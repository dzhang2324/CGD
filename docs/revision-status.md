# Revision status

## Ordered revision checklist

Updated November 12, 2026. Follow the author's manual Find → Replace → explanation → check workflow. Mark an item complete only after verifying the corresponding manuscript edits.

- [ ] **1. Align the methods and equation with the analysis — in progress.**
  - [x] Replace the outcomes/equation block and explain why manufacturer counts cannot be estimated alongside drug-group fixed effects.
  - [ ] Refine paragraph breaks in the new methods text.
  - [ ] Clarify the source data, sample construction, and brand-name/generic-name group definition.
  - [ ] Align the empirical introduction with year controls and specifications with and without log claims.
- [ ] **2. Update the interpretation of the results.** Address significance, model fit, coefficient changes, percentage units, and causal limitations.
- [ ] **3. Remove the obsolete total-spending discussion.** Reconcile the abstract, remove the redundant results paragraph, and resolve the two references to the removed table.
- [ ] **4. Strengthen and correct the literature review.** Address foundational generic-entry studies, FDA attribution, citation accuracy, and the remaining FTC source check.
- [ ] **5. Tighten the supplementary analyses.** Clarify Cost Plus assumptions and shorten NADAC to a supported descriptive discussion.
- [ ] **6. Finish consistency and presentation checks.** Reconcile the abstract and conclusion, complete references, check equations and figures, compile, and save the completed checkpoint.

The shorter writing sample remains deferred. The author has applied the new outcomes, equation, claims motivation, and explanation of why drug-group fixed effects absorb manufacturer counts. This content has been verified; paragraph flow, the data description, and the empirical introduction remain open within item 1.

## Implemented and verified

- Python pipeline, pinned environment, immutable historical inputs.
- Source-panel audit: 16,146 source rows, 80,730 panel rows.
- Regression sample: 12,740 observations, 3,244 brand/generic groups; no duplicate group-years.
- Manufacturer count is invariant within each corrected group; the old brand-only grouping confounded different groups.
- Four Medicaid specifications with year indicators and drug-group clustered uncertainty; no drug fixed effects.
- Two original Cost Plus specifications reproduced with HC3 uncertainty.
- Exact percentage transformations, seven generated tables, three regenerated figures.
- Standalone total-spending results table removed; Cost Plus analysis moved to Appendix A without rewriting its prose.
- Nine meaningful tests passed. All 18 generated artifacts reproduced byte-for-byte in a separate output directory.
- Before the manual editing round, all 29 proposed Find/Replace edits were checked for unique matches and compiled in a temporary copy with the proposed bibliography; no undefined references or overfull boxes remained in that preview.
- Working PDF compiled and new regression/descriptive tables visually inspected.
- Sixteen numerical references were updated in commit `0f62365`, without changing manuscript wording; the PDF was rebuilt. The two claims-volume statements lacking percentage units remain for manual revision.

## Main results

| Outcome | Controls | Manufacturer coefficient | Clustered SE | Percentage association (95% CI) |
|---|---|---:|---:|---|
| Spending per dosage unit | Year | -0.1855 | 0.0085 | -16.9% (-18.3%, -15.5%) |
| Spending per dosage unit | Year + log claims | -0.1302 | 0.0108 | -12.2% (-14.1%, -10.3%) |
| Spending per claim | Year | -0.1697 | 0.0074 | -15.6% (-16.8%, -14.4%) |
| Spending per claim | Year + log claims | -0.0913 | 0.0081 | -8.7% (-10.2%, -7.3%) |

These are associations across drug groups, not causal effects of entry. Results are unweighted pooled OLS. Full precision and model metadata are in `analysis/output/estimates.csv`.

## Requires the author's manual prose edits

The new tables are deliberately not accompanied by automatic interpretation changes. **The current PDF is an intermediate working draft, not a submission-ready paper.**

- Abstract still cites the removed total-spending result and old drug fixed effects.
- The equation block now defines the two retained outcomes, pooled OLS, claims and year controls, clustering, and the reason for omitting drug-group fixed effects. The earlier empirical introduction and source/sample descriptions still need alignment.
- Results paragraphs still contain outdated interpretations of significance, fit, and total spending. The verified numerical references and retained column numbers have been refreshed.
- Two references to the removed `table:table2` are unresolved; deleting/replacing the obsolete paragraphs will resolve both. No labels are duplicated or empty.
- One long raw variable name overflows its line in the obsolete methods paragraph; its proposed prose replacement removes that issue.
- Conclusion and theoretical/literature claims need the revisions in `manual-revisions.md`.
- NADAC remains unrecomputed; its descriptive section and table claims need manual shortening. In particular, the manuscript's 16-row positive-gap table disagrees with saved notebook output (15 rows), and 67% disagrees with its displayed maximum (1.679 as a proportion). Do not present those values as freshly verified.
- Cost Plus prose still needs the construction caveat; the saved CSV has no duplicate medication names despite the old description.
- Bibliography entries are proposed for manual addition, not silently added to the paper.
- FTC source verification remains pending: both FTC homepages and attempted document addresses returned HTTP 404 in this environment. FDA and Brookings source PDFs were read directly; the guide does not insert unverified FTC findings.

## Version checkpoints

- `baseline-before-rewrite` / `c399770`: original source and PDF.
- `cb8bf88`: Python code, tests, and pinned environment.
- `analysis-verified` / `d401a19`: generated results, integrated tables, and the PDF checkpoint `Paper/checkpoints/analysis-updated-pending-prose.pdf`.
- `0f62365`: numerical references refreshed without changing wording; full provenance is in `docs/numerical-updates.json`.
- The revision guides are committed separately from code and numerical changes.

## Next checkpoints

Apply one Find/Replace batch from `manual-revisions.md`, save the source, check the rebuilt PDF, and commit the approved prose. After all required edits, repeat reference/numerical checks and save/tag the completed full-paper revision. The shorter writing sample remains deferred.
