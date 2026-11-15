# Short Medicaid manuscript

The current version is **10 pages of main text** and **13 pages with
references and appendices**. It meets the 10-page maximum through layout
changes alone after the first deletion pass; no additional prose was cut.

The forced page break before the regression analysis and the table barriers
were removed. Figures and regression tables can sit within text pages, without
requesting separate float-only pages. Font sizes, margins, line spacing, figure
sizes, captions, and table contents are unchanged.

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
records the initial deletions and copied assets. Later author edits are
preserved in Git. The layout-only checkpoint is `short-ten-pages`, with its
source and PDF checks recorded in `checkpoints/ten-page-validation.json`.

The working PDFs and LaTeX build files are ignored by Git. Named PDF checkpoints,
source files, figures, and tables are tracked.

The first-pass PDFs are saved in `checkpoints/first-pass-main-12-pages.pdf` and
`checkpoints/first-pass-with-supplement-15-pages.pdf`.
`checkpoints/first-pass-validation.json` records source, asset, reference,
page-count, and rendering checks.

The current PDF checkpoints are `checkpoints/ten-page-main.pdf` and
`checkpoints/ten-page-with-supplement.pdf`. Git tag `before-short-whitespace`
preserves the author-edited 12-page version immediately before the layout change.
