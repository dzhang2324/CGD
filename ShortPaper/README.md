# Short Medicaid manuscript

The first deletion pass is **12 pages of main text** and **15 pages with
references and appendices**. It does not yet meet the 10-page maximum. The
author chose to review this draft before authorizing additional cuts.

Edit `body.tex` for the shared manuscript. The two root documents use the same
body and formatting:

- `main.tex`: main text only, including title, abstract, figures, and tables.
- `with-supplement.tex`: the same main text, followed by references and the
  existing Medicaid appendix tables.

Build from this directory:

```sh
/opt/homebrew/bin/tectonic --only-cached --synctex --keep-logs main.tex
/opt/homebrew/bin/tectonic --only-cached --synctex --keep-logs with-supplement.tex
```

The corresponding working PDFs are `main.pdf` and `with-supplement.pdf`.
All manuscript dependencies are local to this folder; compilation does not need
the full paper or analysis directories.

## Edit with live PDF updates

1. Open `main.tex` in the editor.
2. In the Command Palette, run **LaTeX Workshop: Build LaTeX project**, then
   **LaTeX Workshop: View LaTeX PDF file** to open the working PDF.
3. Edit `body.tex` and save with **Cmd+S**. LaTeX Workshop rebuilds `main.pdf`,
   and its PDF tab updates after the build.

The root-file comment at the top of `body.tex` directs builds to `main.tex`.
Both build entry points contain their own document-class declaration, so
LaTeX Workshop can identify them. A local `.vscode/settings.json` also enables
the same save-to-build behavior when this folder is opened on its own.

To build the version with references and appendices, open
`with-supplement.tex` and use the same Build and View commands. Saves in
`body.tex` target `main.pdf`; rebuild `with-supplement.tex` explicitly to
refresh that version. Saves in `references.tex` or `appendix.tex` target
`with-supplement.pdf`.

Open the working PDFs in this directory for live updates. PDF files under
`checkpoints/` are saved snapshots and do not update.

The full paper is preserved at Git tag `before-short-version`. Its freshly
compiled PDF and source/PDF hashes are in `checkpoints/`. `provenance.json`
records the exact deletions and copied assets. No manuscript wording, results,
table layout, font size, margins, or line spacing were changed.

The working PDFs and LaTeX build files are ignored by Git. Named PDF checkpoints,
source files, figures, and tables are tracked.

The first-pass PDFs are saved in `checkpoints/first-pass-main-12-pages.pdf` and
`checkpoints/first-pass-with-supplement-15-pages.pdf`.
`checkpoints/first-pass-validation.json` records source, asset, reference,
page-count, and rendering checks.
