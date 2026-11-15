# Rimi's feedback and current status

Source: email text pasted by the author on November 13, 2026.
The numbered quotations below preserve the supplied must-fix comments.
Table numbers and coefficients in the email refer to the version Rimi read.
The author now prioritizes Yunus's November 13 review, recorded in
`yunus-feedback.md`. These remaining corrections should support that
Medicaid-centered framing rather than dictate the editing order.

## Author's editing preference

Make the smallest correction needed to address an actual inaccuracy or a
missing point in Rimi's feedback. Preserve existing wording and accurate
descriptions. Do not add a history of coding mistakes merely to explain the
revision. Propose exact Find/Replace edits for the author to apply manually.
Check related passages for consistency, but do not turn that check into a
whole-section rewrite.

The shorter writing sample and optional new analyses remain deferred.

## Must fixes, in Rimi's order

### 1. Manufacturer-count variation

> Check where the variation in manufacturers comes from. Section 2.1 says the count doesn't change over 2017 to 2021, but your fixed effects model still estimates a coefficient. Either the count does change (fix Section 2.1), or the drug ID isn't unique across dosage forms. This is a quick check in your data, and the text should say which it is.

The analysis correction is implemented and verified. The original statement
that the recorded count is time invariant was already accurate. The author
has added the brand/generic group definition; the methods explain why the
count cannot be estimated alongside drug-group fixed effects. The author
also removed drug-name fixed effects from the abstract's model description.
The empirical introduction now correctly describes associations and
year-controlled models with and without log claims. Its obsolete reference
to entity effects is removed; the saved edit was checked on November 15,
2026.

### 2. Standard errors

> Cluster standard errors by drug only. The tables cluster on time too, and with only 5 years that gives unreliable standard errors. This is a one-line change and rerun.

Completed in all four Medicaid models, generated tables, and the revised
methods. No further analysis or explanatory prose is required for this item.

### 3. Redundant total-spending result

> Drop Table 2. Because it controls for log claims, it's the same regression as Table 3 (same -0.124 and SE), so the result is about spending per claim, not total spending. Lead with price per unit and report it as it comes out after the clustering fix.

Completed in the current Medicaid results. The original total-spending table has been removed. The
dosage-unit table appears first. The retained per-claim table is now numbered
Table 2 in the PDF; it is not the removed table.

The author has corrected the abstract to lead with 12.2% lower spending per
dosage unit and then 8.7% lower spending per claim. This was checked against
the current estimates and the controls described in the preceding sentence.

The opening results paragraph now correctly identifies column (1), reports
16.9% and 15.6% lower spending with year controls, and uses association
language. Its obsolete total-spending claim and the following explanation
have been removed; these changes were checked in context.

The paragraph directly describing the removed total-spending regression has
also been deleted and the surrounding outcome paragraphs checked.

The final reference to the removed table is gone. The per-claim paragraph's
log-claims coefficient and percentage interpretation have also been corrected
to -0.245 and approximately 0.245%, and checked against the saved estimates.

The earlier comparison to total spending in the per-claim paragraph has
been deleted, and the conclusion now refers to two cost metrics. Both edits
have been checked against the current source.

The primary dosage-unit manufacturer result has now been corrected and
checked: the coefficient falls in magnitude after adding claims, remains
significant at the 1% level, and corresponds to 12.2% lower spending.
The dosage-unit model-fit and log-claims statements have also been corrected
and checked: adding claims raises R-squared from 0.110 to 0.127, and the
log-claims coefficient is -0.173 (approximately 0.173% lower unit spending
per 1% higher claims). The per-claim model-fit sentence is also corrected
and checked: adding claims raises R-squared from 0.147 to 0.203, with adjusted
R-squared of 0.202. The transition about model controls now correctly
attributes the coefficient and R-squared changes to adding log claims;
the saved edit was checked on November 15, 2026.
The author added the manufacturer-count result to the per-claim paragraph:
8.7% lower spending per claim, statistically significant at the 1% level.
The saved edit was checked on November 15, 2026, and agrees with the current
estimates and abstract.

### 4. Causal language

> Soften the causal language. Generics choose which drugs to enter, so use "is associated with" instead of "causes," and add a short paragraph on this.

In progress. Association language and the short entry-selection limitation
are present in the Medicaid results summary, checked on November 15, 2026.
The Medicaid conclusion now matches the results and no longer uses the
unsupported confirmation, robustness, or R-squared claims. Review the
remaining claims in the introduction to the competition-and-costs section,
the supplementary sections, and their conclusion paragraphs, preserving
surrounding prose where possible.

### 5. Log coefficients

> Fix the interpretation of the log coefficients. -0.124 is about an 11.7% drop (exp(b) minus 1), not 12.4%.

The regenerated results use the exact percentage transformation and earlier
numerical updates are recorded in `numerical-updates.json`. Check that each
retained sentence names the correct outcome and uses the appropriate
percentage units. Both Medicaid log-claims interpretations have now been
checked against the current estimates. The coefficient in Rimi's email is
from the older analysis.

### 6. Supplementary sections

> Cut or shorten the side sections. Move Cost Plus to an appendix (manufacturing cost is on both sides of that regression), and keep the NADAC section to a short descriptive paragraph without "telltale signs of monopoly pricing." This also gets you most of the way to the shorter version.

In progress. Cost Plus is already in Appendix A. Its interpretation still
needs to reflect the constructed cost/markup relationship. NADAC still needs
the requested shortening and descriptive framing. Preserve the author's
recent wording edits when preparing the necessary changes.
The author explicitly chose to retain the higher-cost-generic subgroup
table for now on November 15. Removing that specific table was our editorial
suggestion, not Rimi's instruction. Its numerical discrepancy remains open.
The paragraph beneath the NADAC gap histogram now describes the observed
gap and no longer claims unnecessary pricing, profitability, or monopoly
pricing. This saved edit was checked on November 15; the NADAC summary and
conclusion were the next items. The author has now revised the NADAC summary
to describe paired acquisition-cost gaps in 2019, preserving the 80% observation
and exceptions and removing entry-effect, consumer-cost, and computing-difficulty
claims. The saved summary was checked on November 15; the NADAC conclusion
has now also been revised and checked on November 15. It reports the
descriptive findings in the overall and paired comparisons without an
entry-effect claim. Cost Plus construction and interpretation are the
next major outstanding issue.
The Cost Plus paragraph preceding the markup formula now identifies
manufacturing cost as estimated from the pricing rule and explains that
it also enters the markup denominator. This saved edit was checked on
November 15. The subsequent regression interpretations and Cost Plus
conclusion still require alignment with that limitation.
The author explicitly requested that the manuscript explain the denominator
mechanism and its implications for interpretation. Do not suggest that the
entire negative coefficient must be mechanical. Distinguish the markup
regression from the separate retail-price regression, which does not share
that denominator construction but still uses an inferred cost proxy.
On November 15, after discussing the limited contribution of the markup
result, the author explicitly chose to remove the markup regression rather
than expand its qualifications. Supply exact deletion blocks for the author
to apply. Remove its calculation, table, interpretation, figure panel, and
summary/conclusion claims; retain the retail-price analysis for now and
preserve historical inputs, code, and outputs. This specific deletion is
our proposed implementation, not an explicit reviewer instruction.
The markup-regression block and figure panel are now removed, with the
historical results preserved. The conclusion gives a short linked summary
of the retained retail analysis and finishes with the Medicaid contribution
and policy motivation. The retained retail-regression paragraph in Appendix A
is now corrected: its unsupported coefficient threshold is removed, model
fit refers to log retail prices, and the interpretation is descriptive and
qualified by the inferred cost measure. The conclusion's added acquisition-
cost implication, possible demand explanation, and conditional entry-policy
discussion are reviewed. The competition-and-costs section opening is now
corrected and the saved edit verified. A single-sentence correction to the
scope of the monopoly/perfect-competition comparison is proposed next; it
is our consistency observation, not a separate theoretical correction
specifically requested by Rimi.
That theory sentence has now been revised and checked. The next proposed
Data-section correction distinguishes the 16,146 source records (including
manufacturer-specific and Overall rows) from distinct drug groups and from
the 12,740-observation regression sample.
That first data-paragraph correction is now saved and verified. The omitted
spending-per-claim covariate is now in the dictionary and both narrative
counts correctly state eleven base-panel covariates, including Year.
The dictionary already contained Year; the summary-statistics tables need
no additional Year row. The author wants to move on from these small
details. A remaining substantive measurement clarification is that the
CMS spending outcomes include dispensing fees and are before manufacturer
rebates. This is a source-based consistency observation, not a separate
correction explicitly requested by Rimi.
The author has now inserted that definition, including the CMS (2022)
attribution, and the saved edit is verified.

### 7. Literature and presentation

> Add the core generic entry papers (Caves, Whinston and Hurwitz 1991; Reiffen and Ward 2005; the FTC work on the number of generic entrants), and fix the broken tables, equations, and repeated text in the Data section.

In progress. The author added Caves, Whinston, and Hurwitz and expanded
the Reiffen and Ward discussion to cover competition, prices, and expected
market size; the saved introduction paragraph was checked on November 15,
2026. Source notes exist for further literature corrections. The
bibliography in `Paper/references.tex` is now included after the conclusion
and has been checked in the rebuilt PDF. The FTC record and full working paper for Reiffen and
Ward have now been verified: the 2002 working paper is the earlier version
of the published 2005 article already cited. No duplicate reference or
new literature paragraph is needed. The main regression equation is
corrected.
The two references to the removed total-spending table have been removed.
Review actual repetition and errors in the data section without rewriting
accurate material.

## Rimi's qualification and optional work

> If point 1 turns into a bigger fix, it's fine to just explain clearly where the variation comes from and frame the results as associations/descriptives. Building this dataset yourself is a real signal to adcoms, so it's worth the cleanup.

> If you have time (not needed for the applications): bins for the number of manufacturers (1, 2, 3, 4 to 5, 6+), results with and without the claims control, and an event study around first generic entry.

The current models already include specifications with and without log
claims. New binned specifications, an event study, and a shorter sample are
outside the current editing round.
