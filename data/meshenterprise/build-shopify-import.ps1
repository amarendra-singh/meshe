$source = Import-Csv -LiteralPath (Join-Path $PSScriptRoot 'products.csv')
$output = Join-Path $PSScriptRoot 'shopify-import.csv'
$rows = [System.Collections.Generic.List[object]]::new()

foreach ($product in $source) {
    $title = switch ($product.title) {
        'Silime track car' { 'Slime Track Car' }
        'Greedy Sanke Game' { 'Greedy Snake Game' }
        '!n+31ligent car' { 'Intelligent Car' }
        default { $product.title }
    }
    $type = switch ($product.category) {
        'EXCLUSIVE GADGETS' { 'Interactive Gadgets' }
        'Remote control Toys' { 'Remote Control Toys' }
        'Educational Toys' { 'Educational Toys' }
        default { 'Puzzles & Play' }
    }
    $handle = ($title.ToLowerInvariant() -replace '[^a-z0-9]+', '-').Trim('-')
    $images = @($product.image_urls -split ' \| ')
    for ($i = 0; $i -lt $images.Count; $i++) {
        $row = [ordered]@{
            'URL handle' = $handle
            'Title' = if ($i -eq 0) { $title } else { '' }
            'Description' = if ($i -eq 0) { '<p>' + [System.Net.WebUtility]::HtmlEncode($product.description) + '</p>' } else { '' }
            'Vendor' = if ($i -eq 0) { 'Mesh Enterprise' } else { '' }
            'Type' = if ($i -eq 0) { $type } else { '' }
            'Tags' = if ($i -eq 0) { 'mesh-source-2026-10-22' } else { '' }
            'Published on online store' = if ($i -eq 0) { 'false' } else { '' }
            'Status' = if ($i -eq 0) { 'draft' } else { '' }
            'Option1 name' = if ($i -eq 0) { 'Default Title' } else { '' }
            'Option1 value' = if ($i -eq 0) { 'Default Title' } else { '' }
            'SKU' = if ($i -eq 0) { $product.sku } else { '' }
            'Price' = if ($i -eq 0) { $product.price_inr } else { '' }
            'Compare-at price' = if ($i -eq 0) { $product.compare_at_inr } else { '' }
            'Requires shipping' = if ($i -eq 0) { 'true' } else { '' }
            'Fulfillment service' = if ($i -eq 0) { 'manual' } else { '' }
            'Product image URL' = $images[$i]
            'Image position' = $i + 1
            'Image alt text' = $title
        }
        $rows.Add([pscustomobject]$row)
    }
}

$rows | ConvertTo-Csv -NoTypeInformation | Set-Content -LiteralPath $output -Encoding utf8
Write-Output "Products: $($source.Count); image rows: $($rows.Count); output: $output"
