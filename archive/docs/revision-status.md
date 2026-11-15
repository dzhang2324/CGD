# Revision status

## Current editing scope

The author now prioritizes Yunus's November 13 feedback, retrieved from
Rimi's forwarded email. The exact comments and updated working order are in
`yunus-feedback.md`: center one Medicaid research question, address the
abstract and introduction first, then align identification, supplementary
material, and presentation. Rimi's remaining corrections still apply.

The author subsequently authorized the assistant to apply the eight final
terminology replacements after first saving and committing a checkpoint.
That checkpoint is `before-terminology-cleanup` (`5cfadb0`). The replacements
are complete and verified; this specific authorization does not change the
manual workflow for other prose revisions.

The author's November 13 instruction is to preserve existing prose and make
minimal corrections tied to Rimi's actual comments. An accurate existing
description does not need expansion merely because a coding error was fixed.
Check surrounding passages, then propose only necessary, focused edits.
The exact seven must-fix comments and their current status are recorded in
`rimi-feedback.md`. Yunus's priority overlay now governs the next edits.

On November 15, the author emphasized staying focused on the agreed
big-picture items: NADAC interpretation, Cost Plus interpretation, the
paper's Medicaid-centered focus, references, and necessary consistency
and presentation checks. Do not drift into minor stylistic polishing or
reopen settled wording. Within those priorities, propose focused manual
edits and explain the substantive issue they resolve.

The author subsequently requested stronger interpretation in the Cost Plus
discussion and the conclusion. A numerical recap followed only by caveats
is insufficient: explain the economic meaning and potential implications
first, then discuss the concrete reasons the interpretation may be
incomplete. Present untested mechanisms and policy implications as tentative
interpretations, while preserving the distinction between the observed
associations and causal effects. This is an authorized substantive revision
of the recently reviewed conclusion, not a request for general polishing.
The author clarified that the additional interpretation should focus on the
NADAC and Cost Plus conclusion summaries. Preserve the existing closing
paragraph, especially its final two sentences. Add concrete examples of
demand and production characteristics with a focused insertion rather than
replacing that paragraph. The next proposed edits are three single-sentence
insertions, not another full conclusion rewrite.
The saved conclusion now includes the acquisition-cost implication, a
possible demand/competing-products explanation, and a conditional policy
interpretation. These author-edited passages are reviewed and acceptable.
The illustrative list of entry factors was not inserted; it is optional,
not an outstanding required correction. Do not reopen the conclusion now.

The author subsequently specified a minimum of **15 pages of main text**,
excluding references and appendices. Preserve useful material and avoid
unnecessary shortening. If expansion is needed, develop the substantive
Medicaid argument and methods rather than adding padding or inflating layout.
Proposed additions remain subject to the manual editing workflow.

The author wants the Cost Plus appendix identified by a clickable reference
in the introduction, with a brief summary of its retained retail-price
finding at the end of the conclusion. Keep the detailed interpretation in
the appendix. The appendix label, introduction reference, obsolete
conclusion paragraph deletion, and closing summary are now verified in the
saved manuscript. The author revised the proposed numerical recap to a
higher-level takeaway about the cost-price relationship. The reference
syntax was previously compiled in a temporary preview and resolves to A.
The author now requests broader concluding commentary: connect the Medicaid
findings to affordability, public spending, and the contribution of the
constructed panel. That addition is now saved and reviewed, including the
author's point that understanding entry selection can inform causal research
designs. The conclusion preserves the descriptive interpretation of the
current estimates. Its existing wording is acceptable; do not reopen it
for minor stylistic or repetition edits. The PDF rebuilt successfully and
the Cost Plus appendix link resolves to Appendix A on page 16.

The current PDF has 24 pages, with References on page 17 and Appendix A
starting on page 18. Pages 1--16 precede the references, but page 1 includes
the title and abstract and the final main-text page is only partly filled. Check the author's
15-page main-text requirement separately from the references and appendices.
If additional depth is needed, prioritize useful explanation of Medicaid
sample construction, measurement, and the existing results.

## Ordered revision checklist

Updated November 15, 2026. Follow the author's manual Find → Replace → explanation → check workflow. Mark an item complete only after verifying the corresponding manuscript edits.

- [x] **1. Align the methods and equation with the analysis.** The outcomes, year controls, claims motivation, drug-group clustering, time-invariant manufacturer counts, and absence of drug fixed effects are explained. The empirical introduction and group definition are corrected.
- [x] **2. Correct the main Medicaid results interpretation.** The retained outcome paragraphs, percentage conversions, significance and model-fit descriptions, entry-selection limitation, and Medicaid conclusion are aligned with the current models.
- [x] **3. Remove the obsolete total-spending result.** The redundant table, associated discussion, and references are gone.
- [x] **4. Complete the agreed substantive abstract/introduction revisions.** Center the Medicaid question, motivate innovation and affordability, explain the dataset contribution, and integrate the generic-entry literature. Do not reopen this as a general rewrite.
- [x] **5. Finish the agreed supplementary-analysis revisions.** The NADAC comparisons are framed descriptively, and the author explicitly retains the subgroup table's count of 16. The Cost Plus markup regression, figure panel, discussion, summary-statistics row, and dictionary entry are removed; the retail-price analysis remains in the appendix. Historical inputs, code, and regression outputs are preserved. The separate final data-description checks below remain open.
- [x] **6. Complete references.** The FTC source check is resolved, the formal reference list is included, and the PDF compiles without unresolved-reference warnings.
- [x] **7. Finish the agreed consistency and presentation checks.** The competition-section opening, data descriptions, covariate names, equations, figures, numerical references, and PDF layout have been checked; the completed terminology revision has a saved PDF checkpoint.
  - [x] Add concise, explicit dependent-variable headers to all four regression tables.
  - [x] Verify the author's added definition that Medicaid spending includes dispensing fees and is not reduced by manufacturer rebates.
  - [x] Include `Paper/references.tex` after the conclusion. The list covers the retained citations and credited course-note/figure sources; the author's insertion is verified.
  - [x] Apply the approved table format after securing the checkpoint. Tag `before-econometrica-formatting` at `1ae3c08` preserves the exact manuscript, references, generated tables, and saved PDF before formatting. The approved Econometrica-style layout now applies to regression, summary, and covariate-description tables; readable labels replace raw codes inside tables. Captions and rules are consistent, definitions and values are unchanged, and the PDF has been visually checked.
  - [x] Replace raw manufacturer-count, claims, and NADAC codes in the results, and align the Cost Plus equations with the table labels. The author's saved edits are verified.
  - [x] Finish the remaining terminology cleanup: the two `Outlier\_Flag` references and residual uses of features/variables for covariates. All eight authorized replacement rules were applied, covering 18 occurrences.
  - [x] Complete four focused Cost Plus corrections: the unsupported duplicate-row claim, the contradictory shipping reference, the assumed equivalence to the supply-chain figure's cost components, and the obsolete appendix-title reference. The author's four saved replacements are verified.
  - [x] Finish the PDF layout/page-count check and save the completed revision checkpoint. The PDF compiles without LaTeX warnings and remains 24 pages, with References on page 17 and Appendix A on page 18. The appendix heading overflow is fixed, and the updated PDF is saved as `Paper/checkpoints/terminology-cleanup-complete.pdf`.

The shorter writing sample, manufacturer bins, event study, and additional analyses remain deferred. Medicaid-centered ordering of the overall conclusion would support Yunus's focus request, but is our suggested implementation rather than a specific instruction from him.

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
- Sixteen numerical references were updated in commit `0f62365`, without changing manuscript wording; the PDF was rebuilt. The two claims-volume statements and their percentage units have since been corrected manually and checked.
- All four regression tables identify the dependent variable above the numbered columns: Log spending per unit, Log spending per claim, Log retail price, and Log markup. Notes specify natural logarithms and clarify the weighted per-unit measure. The PDF was rebuilt and all four headers were visually checked; the existing numerical outputs and table results are unchanged.
- The author removed the Cost Plus markup-regression calculation, table, and discussion from the appendix. Historical code and outputs remain preserved. The author has substituted the generated, visually checked retail-only log scatterplot, `analysis/output/figures/costplus_retail_log.pdf`, for the two-panel figure; the saved source is verified and the PDF rebuilt. The retained retail-regression table note no longer describes the removed markup outcome. A fresh pipeline run passed its audit; all existing outputs except that table note were unchanged, and only the new figure was added.
- The author approved the Econometrica-style preview and required a checkpoint first. The checkpoint was committed and the clean worktree, tagged source hashes, and saved PDF were verified before table editing began. After formatting, all non-table analysis artifacts are byte-identical to that checkpoint, including numerical results and figures. Nine tests passed. Narrative text, equations, dictionary definitions, NADAC values, and internal references are unchanged. The full PDF compiles with no unresolved-reference or table-overflow warnings; the existing long Cost Plus appendix heading still produces a horizontal overflow warning.

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

- The abstract, agreed introduction, methods, main Medicaid results, and Medicaid conclusion are aligned. Remaining work concerns supplementary claims, data-description checks, references, and presentation.
- The competition-section opening now correctly introduces theory and associations between reported manufacturer counts and both Medicaid spending outcomes. The saved edit is verified. The theory paragraph now treats the monopoly/perfect-competition comparison as motivation for the relationship rather than a universal rule; that saved edit is also verified.
- No references to the removed `table:table2` remain. The obsolete discussion and model-control comparisons are corrected. No labels are duplicated or empty.
- The overall conclusion now starts with Medicaid, includes the NADAC acquisition-cost implications and a short linked Cost Plus interpretation, and closes with a conditional policy implication, dataset contribution, and entry-selection research direction. The author's latest revisions are checked and the PDF rebuilt. The retained retail-regression paragraph now correctly reports the coefficient and model fit in log retail prices, removes the unsupported coefficient-at-least-one benchmark, and explains the inferred cost measure and limits of interpretation. The competition-and-costs opening and theory transition are also corrected. Proposed older Find blocks must be rechecked against current text before use.
- The first Medicaid data paragraph is now corrected and the saved edit verified: 16,146 source records include individual-manufacturer and Overall records, rather than representing 16,146 distinct drugs. Reshaping yields 80,730 rows, including missing annual data; the filtered analysis has 12,740 observations across 3,244 groups. The source audit additionally confirms 11,802 manufacturer-specific records and 4,344 Overall records. The spending-per-claim dictionary entry and both references to eleven base-panel covariates are now saved and verified. The dictionary already includes Year; the summary-statistics tables intentionally report substantive numeric measures and need no additional Year row. Move on from counting and terminology details. The author has now added the verified definition that CMS spending includes dispensing fees and is not reduced by manufacturer rebates, citing CMS (2022). The next proposed step is the formal reference list.
- NADAC remains unrecomputed. The author explicitly instructs retaining 16 in the subgroup table; do not reopen that count as a required edit. The saved notebook's 15-row result remains a historical discrepancy, not an independently verified reconciliation. The NADAC gap and proportional-gap definitions now match the table labels and the saved formulas.
- The author removed the constructed-markup covariate from the Cost Plus description and dictionary. Its generated summary row and note have also been removed through the report generator. A fresh analysis run passed the audit; all retained summary values and all other analysis outputs were unchanged. The two Cost Plus equations now use matching readable labels.
- The four focused Cost Plus corrections are saved and verified. The retained regression already explains that manufacturing cost is inferred from the pricing rule; no new interpretation paragraph is needed.
- The final terminology edit is an exact match to the eight authorized replacements applied to the pre-edit checkpoint. All numerical text and all scientific code, data, and result files remain unchanged by that edit. The compiled PDF and representative edited pages have been checked.
- `Paper/references.tex` contains twelve alphabetized references matching the retained citations, course-note attribution, and textbook figure source. The author has included it between the conclusion and appendices. The working manuscript rebuilt successfully: the reference list fits on page 16, Appendix A starts on page 17, and there are no unresolved-reference warnings.
- The FTC source check is resolved for Reiffen and Ward's directly relevant paper: the official FTC record and full working paper identify the 2002 working-paper version of the published 2005 study already cited. The prepared reference list retains the published version; no extra literature paragraph is needed. The unrelated authorized-generics report is not treated as verified.

## Version checkpoints

- `baseline-before-rewrite` / `c399770`: original source and PDF.
- `cb8bf88`: Python code, tests, and pinned environment.
- `analysis-verified` / `d401a19`: generated results, integrated tables, and the PDF checkpoint `Paper/checkpoints/analysis-updated-pending-prose.pdf`.
- `0f62365`: numerical references refreshed without changing wording; full provenance is in `docs/numerical-updates.json`.
- `37c302b` and `0722748`: approved methods/equation revision and paragraph consolidation.
- `bdb9fcf`: reproducible dependent-variable header generation; regenerated tables are committed separately.
- The revision guides are committed separately from code and numerical changes.

## Next checkpoints

Apply one Find/Replace batch from `manual-revisions.md`, save the source, check the rebuilt PDF, and commit the approved prose. After all required edits, repeat reference/numerical checks and save/tag the completed full-paper revision. The shorter writing sample remains deferred.
