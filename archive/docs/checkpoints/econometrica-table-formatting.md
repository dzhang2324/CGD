# Approved table-formatting checkpoint

The author approved `docs/table-style-preview/preview.pdf` and required
version control before implementation. The pre-formatting state was
committed and verified under `before-econometrica-formatting` (`1ae3c08`)
before any table editing began.

The formatted PDF is saved as:
`Paper/checkpoints/econometrica-table-formatting.pdf`.

Changes:

- Consistent table-number and title layout.
- Clear outcome headings, numbered model columns, and standard errors
  below coefficients.
- Booktabs rules and consistent spacing across summary and dictionary tables.
- Readable covariate labels inside tables; raw analysis column names are
  unchanged in the data and code.

Validation:

- Nine existing tests passed.
- The analysis audit passed.
- Numerical, audit, data, and figure outputs are byte-identical to the
  pre-formatting state.
- Narrative paragraphs, equations, dictionary definitions, NADAC numbers,
  and internal labels are unchanged.
- The full PDF compiles and table pages were inspected visually.
- The existing long Cost Plus appendix heading still has a horizontal
  overflow warning; no table-overflow or unresolved-reference warning remains.

Raw covariate names in narrative prose await the manual editing workflow.
The NADAC subgroup discrepancy and other previously recorded factual checks
remain open.
