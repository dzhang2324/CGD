# Competition and Generic Drugs

Research on manufacturer competition and Medicaid drug spending, with a full
paper, a separate short writing sample, and reproducible Python analysis.

## Read or edit the papers

| Version | LaTeX source | Saved PDF |
| --- | --- | --- |
| Full paper | [Paper/main.tex](Paper/main.tex) | [Full paper](Paper/pdf/full-paper.pdf) |
| Short paper: 10 pages | [ShortPaper/body.tex](ShortPaper/body.tex) | [Short paper](ShortPaper/pdf/short-paper.pdf) |
| Short paper with references and appendices: 13 pages | [ShortPaper/with-supplement.tex](ShortPaper/with-supplement.tex) | [Short paper with supplement](ShortPaper/pdf/short-paper-with-supplement.pdf) |

The two short versions share the same main text. `ShortPaper/` contains its own
figures, tables, and editor settings; editing it does not change the full paper.
See [the short-paper guide](ShortPaper/README.md) for live PDF updates.

## Repository layout

| Directory | Contents |
| --- | --- |
| `Paper/` | Current full-paper source, figures, and saved PDF |
| `ShortPaper/` | Standalone short-paper source, assets, saved PDFs, and local history |
| `analysis/` | Current Python pipeline and reproducible results |
| `data/` | Preserved source data, historical validation panel, and data notes |
| `tests/` | Data-construction and statistical-inference checks |
| `docs/` | Current analysis and reproduction documentation |
| `archive/` | Original notebooks, R code, drafts, revision records, and older full-paper checkpoints |

## Reproduce the analysis

Use Python 3.13 and the pinned dependencies. Run from the repository root:

```sh
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m analysis.run
python -m pytest -q
```

The pipeline reads the saved files in `data/`; it does not download data or
modify inputs. It writes results, audit records, tables, and figures to
`analysis/output/`. The full paper includes its generated tables and figures
from that directory.

For a separate reproduction without overwriting the saved results:

```sh
python -m analysis.run --output-dir /tmp/cgd-reproduction
```

See [analysis details](docs/analysis.md) and [data provenance](data/README.md).
The short paper uses independent copies of its tables and figures; rerunning
the analysis does not overwrite those copies.

## Compile the papers

With Tectonic installed and available on `PATH`:

```sh
(cd Paper && tectonic --synctex --keep-logs main.tex)
(cd ShortPaper && tectonic --synctex --keep-logs main.tex)
(cd ShortPaper && tectonic --synctex --keep-logs with-supplement.tex)
```

On the author's Mac, Tectonic is at `/opt/homebrew/bin/tectonic`. The existing
LaTeX Workshop settings use that path and rebuild on save. Other machines may
need to change the executable path in `.vscode/settings.json` and
`ShortPaper/.vscode/settings.json`.

The working PDFs beside the LaTeX source update when built and are ignored by
Git. PDFs under each paper's `pdf/` directory are tracked snapshots for reading;
they must be refreshed after manuscript edits.

## History

The [archive guide](archive/README.md) identifies historical material. Archived
code and revision proposals are preserved for reference and are not the current
analysis or editing instructions. The original data and relocated historical
files are unchanged; [the relocation manifest](archive/relocation-manifest.json)
records their former paths and SHA-256 hashes.

Git tag `before-repository-cleanup` preserves the layout before this
reorganization. Earlier manuscript checkpoints and tags remain available.
The archive is tracked in Git and is included when this repository is pushed.
