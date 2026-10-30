# Package tooling

The HTML handbook, gallery and wireframes open locally without a server, JavaScript package install or network connection. Images and links use package-relative paths.

Python tooling is optional:

- `validate_package.py`: checks packaged hashes, local links, JSON and required design/content invariants. Uses Python standard library. Original source comparison is additionally performed when the original workspace files are accessible.
- `audit_handoff.py`: decodes all images/vectors, checks copy and action mappings, verifies local runtime resources, then validates a temporary renamed folder copy without the original workspace. Requires Pillow. It does not edit any image.
- `build_viewers.py`: regenerates the HTML documentation from package Markdown/JSON. Requires Python `markdown`. Does not edit any image.
- `build_package.py`: original authoring-workspace seed script. Requires original source files and Pillow. It now refuses to reseed an existing frozen handoff, preventing accidental overwriting of later documented decisions. Do not use it to update this package or expect it to download missing assets.
- `browser-qa.js` and `browser-final-check.js`: Tabbit browser programs. Start from a root HTML page in this handoff, or set `globalThis.meshHandoffBaseUrl` to its file-directory URL before running. They no longer require the original workspace path.
- `browser-receiving-audit.js`: latest browser program, including asset decoding, all 14 handbook chapters and eight responsive widths. Start from START-HERE.html. Its returned measurements are recorded in verification/receiving-ai-browser-checks.json; QA screenshots are in assets/verification/.

Do not regenerate authoritative images. To update documentation, edit the relevant Markdown/data file, regenerate viewers and run validation. Keep the project as a browsable folder; create an archive only if the user explicitly requests one. Validate image checksums before and after; retain the source approval history.
