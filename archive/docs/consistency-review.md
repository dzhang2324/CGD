# Manuscript consistency review

Reviewed November 13, 2026, before continuing the author's manual editing workflow.

**Subsequent author direction:** the groupings below identify passages to
check together, not paragraphs to rewrite together. Preserve accurate original
wording and make small corrections tied to Rimi's actual comments. The
current ordered feedback is recorded in `rimi-feedback.md`.

## Scope and status

Read the complete current `Paper/main.tex`, the seven generated LaTeX tables,
the saved analysis audit and model results, the analysis definitions, the
literature-verification notes, and all 29 prepared manual edits. Checked the
author's uncommitted changes rather than assuming the last commit was current.
Built a separate PDF without replacing the working PDF.

The revised regression equation, methods paragraph, and generated regression
tables agree with the implemented analysis. The surrounding manuscript is
not yet consistent with them. Several older passages and proposed edits need
to be handled together.

**No manuscript wording, analysis, numerical outputs, or working PDF was changed
in this review.** This file records findings and dependencies; it is not a list
of completed prose changes. Line references below identify the reviewed snapshot
and will move as the author edits.

## Rimi comments available verbatim

**Comment 1:**

> Check where the variation in manufacturers comes from. Section 2.1 says the count doesn't change over 2017 to 2021, but your fixed effects model still estimates a coefficient. Either the count does change (fix Section 2.1), or the drug ID isn't unique across dosage forms. This is a quick check in your data, and the text should say which it is.

The data check and model correction are complete. Brand-name-only identifiers
combined distinct brand/generic pairs. Under the corrected pair definition,
reported manufacturer counts are constant within all 3,244 analysis groups.
The source provides a single count repeated across the years, not annual
observations of entry and exit. This does not establish that actual market
counts never changed. The new methods explain the estimation consequence;
the data description and other old model descriptions still require alignment.
Do not attribute the coding issue specifically to dosage forms without evidence.

**Comment 2:**

> Cluster standard errors by drug only. The tables cluster on time too, and with only 5 years that gives unreliable standard errors. This is a one-line change and rerun.

This is complete in all four Medicaid regressions, their tables, and the
revised methods: standard errors are clustered only by the corrected drug
group. Year fixed effects remain. Year fixed effects and year clustering
must not be conflated.

Other issues below are consistency findings or topics in the saved revision
guides. They should not be attributed to a specific additional Rimi comment
without checking her original wording.

## Consistent analysis to preserve

- Medicaid analysis unit: a reported brand-name/generic-name group in a year.
  This is not guaranteed to identify a unique strength, formulation, or NDC.
- Source: 16,146 wide rows, including manufacturer-specific and aggregate rows.
  Reshaping yields 80,730 records, including records with missing annual data.
- Estimation sample: 12,740 observations across 3,244 groups, no duplicate
  group/year rows, and no within-group variation in reported manufacturer count.
- Outcomes: log reported weighted spending per dosage unit and log spending
  per prescription claim.
- Estimator: unweighted pooled OLS, year controls, with and without log claims;
  no drug fixed effects; standard errors clustered by drug group.
- Claims are observed utilization. Including them does not establish that
  demand is exogenous or fully controlled.
- Cost Plus uses the saved 442-row snapshot, inferred costs, and constructed
  markups. NADAC results were not re-estimated.

| Outcome | Year controls only: manufacturer coefficient | With log claims: manufacturer coefficient | Percentage association with log claims |
|---|---:|---:|---:|
| Spending per dosage unit | -0.1855 | -0.1302 | 12.2% lower |
| Spending per claim | -0.1697 | -0.0913 | 8.7% lower |

All four manufacturer coefficients are statistically significant at the
1% level using the implemented clustered inference. The percentage values
use `100 * (exp(beta) - 1)`. They are conditional associations across groups,
not estimated causal effects of entry.

## Findings and connected edits

### 1. Medicaid data description and dictionary

Locations: `Paper/main.tex:52`, `:54`, `:57`, `:59`, and `:289`–`:307`.

- The opening paragraph conflates source rows with distinct drugs and describes
  duplicates without explaining manufacturer-specific versus aggregate records.
- Replacing only the second paragraph would leave the preceding ambiguity and
  remove the enumeration needed by the later phrase “The last two features.”
- The detailed IQR/outlier construction is not established by the saved
  implementation. What is verified is retention of the supplied zero flag.
- The reshaped panel has 11 columns. The dictionary lists ten because it omits
  `Avg_Spnd_Per_Clm`, a principal outcome.
- The manufacturer-count definition should identify the single reported count.
  The weighted dosage-unit outcome should not be presented merely as the ratio
  of aggregate spending to aggregate dosage units.
- The dictionary's outlier entry points to details “below,” although the
  explanation is earlier in the paper.

**Editing unit:** the complete Medicaid data subsection and affected dictionary
entries. Retain a logical order: source/coverage, identifiers/count measurement,
sample filters, then variable definitions and table references. This is the
direct manuscript follow-through on Rimi comment 1.

### 2. Model description across sections

Locations: `:30`, `:76`, `:99`, `:115`–`:122`, and `:223`.

- The abstract still names drug-name fixed effects.
- The empirical introduction still describes a naive regression followed by
  time/entity effects and calls claims “demand.”
- The revised equation and estimation paragraph correctly describe the actual
  four models.
- The conclusion still refers to three outcomes and broadly controlling demand.

**Editing unit:** align the old model descriptions with the approved equation.
Preserve the author's current methods text. The data section explains how the
count is recorded; the methods explain why that prevents a within-group
manufacturer-count estimate. That limited repetition serves distinct purposes.

### 3. Medicaid results, summaries, and interpretation

Locations: `:30`, `:109`, `:134`–`:146`, and `:223`.

- Total-spending/third-regression discussion remains despite removal of the
  table. Two references to `table:table2` are unresolved.
- The dosage-unit result is still described as insignificant and as showing
  little or no relationship, contrary to the new estimates.
- Both outcome discussions say model fit fell after adding claims. R-squared
  actually rises from 0.110 to 0.127 for the dosage-unit model and from 0.147
  to 0.203 for the per-claim model.
- The claims statements “0.03 decrease” and “0.02 decrease” have obsolete
  numbers and no meaningful percentage units. The current log-claims
  coefficients are -0.1728 and -0.2451; their interpretation is an elasticity
  association, not a demand effect.
- Changes in coefficients do not prove that omitted-variable bias was removed.
  Low R-squared does not show that the cited literature exaggerated the
  effect of monopoly power.
- A descriptive plot does not establish a three-manufacturer competitive
  threshold, an exponential pricing relationship, or statistically significant
  changes between manufacturer-count categories.
- The theory, results, and conclusion must distinguish a predicted negative
  relationship from an identified causal effect of entry.

**Editing unit:** retained outcome paragraphs, removal of the obsolete outcome,
the relevant descriptive-plot/theory links, and corresponding abstract and
conclusion statements. Do not change a result paragraph while leaving its old
headline interpretation in the abstract or conclusion.

### 4. Literature, claims, and references

Locations: `:33`–`:46`, `:78`, and `:95`.

These issues were checked against the saved literature-verification notes,
not a fresh external literature search.

- The FDA attribution/percentage sequence does not match the verified report
  described in those notes.
- Pivotal-trial costs and full drug-development costs are distinct quantities.
- The Keyhani attribution overstates what the development-time study addresses.
- “Daalen”/“Janssen Daalen” and 2016/2021 are inconsistent.
- The new generic-entry discussion and other author-year references have no
  bibliography in the current manuscript.
- Figure provenance and the remaining FTC source check are still open.

**Editing unit:** each literature claim together with its citation/bibliography
entry and any sentence or figure introduction that depends on it. Do not
introduce evidence attributed to a source that has not been verified.

### 5. Cost Plus throughout the paper

Locations: `:62`–`:70`, `:221`, `:229`–`:273`, and `:329`–`:341`.

- The source description claims duplicate medication rows, but the audit finds
  none in the saved sample.
- Shipping is described as included and then excluded.
- The data description, appendix, and conclusion alternate between inferred
  manufacturing costs and costs that are treated as known.
- The supply-chain illustration does not establish what the inferred cost
  measure includes.
- The dictionary defines markup as a percentage from `CP_price` to
  `retail_price`. The implemented formula is
  `100 * ((retail_price - 3) / estimated_cost - 1)`.
- The dictionary points to a former section title, “Manufacturing Costs and
  Pricing.” The appendix now has a different title.
- The appendix opener “I will first investigate” reflects its earlier position.
- Across-product log slopes and the constructed markup do not establish how
  prices respond to changing costs or measure intellectual-property rents.
  Cost also appears in the markup denominator.
- Corresponding abstract and conclusion language must remain consistent with
  the appendix's assumptions and limited interpretation.

**Editing unit:** source description, formulas, appendix interpretation,
dictionary, and matching summary passages.

### 6. NADAC throughout the paper

Locations: `:73`, `:148`–`:218`, `:225`, and `:361`–`:401`.

- A 2019 comparison is repeatedly described as a price change following generic
  introduction, although the analysis does not establish a before/after design.
- Acquisition costs, patient payments, profits, and monopoly pricing are
  different objects; the current discussion moves between them.
- “67%” conflicts with a displayed maximum proportional gap of 1.679.
- The subgroup labeled “generic is more expensive” includes a negative minimum
  difference. Its 16 observations also disagree with the saved historical
  notebook result discussed in the existing audit notes.
- The source says 12 features, while the dictionary lists 11.
- Normal-looking log distributions do not establish normal raw-cost distributions.
- Removing detailed results while retaining all their tables and appendix
  material would leave an inconsistent account of what the paper presents.

**Editing unit:** supported descriptive claims, associated figures/tables,
source description, relevant appendix material, and the conclusion. Missing
raw-data recovery remains deferred. Do not call these numerical results freshly
verified or automatically replace disputed numbers.

## Prepared replacements need contextual revision

Of the 29 saved Find blocks:

- 26 still match the current manuscript exactly once.
- Item 7 has already been applied; its old Find block should not match.
- Item 20, the Cost Plus conclusion, is stale after the author's changes.
- Item 21, the complete NADAC section, is stale after the author's changes.

An exact match is not sufficient evidence that a replacement is ready. The old
guide also misses the dictionary dependencies and the dangling “last two
features” issue. Before each future batch, obtain its Find text from the current
file, read the complete affected section and summary statements, and prepare
the replacements as a connected unit. Do not overwrite the author's recent
wording with an older proposed block.

## Validation and next editing sequence

The separate cached Tectonic build completed with 28 pages. All input/image
paths exist and no labels are duplicated. Remaining build issues:

- `table:table2` is referenced twice, at source lines 142 and 144, but is no
  longer defined.
- The Cost Plus appendix title overflows by about 11 points at line 229.
- Two underfull boxes remain in dictionary tables at lines 309 and 383.

The successful build does not establish that the prose or historical NADAC
numbers are correct. No regression rerun was required for this review.

Continue the manual workflow in this order:

1. Medicaid source subsection and dictionary, plus the old model descriptions
   needed to finish Rimi comment 1.
2. Medicaid outcomes, results interpretation, and matching abstract/conclusion
   claims, including removal of obsolete total-spending references.
3. Theory/literature claims and their verified citations.
4. Cost Plus as one connected supplementary-analysis revision.
5. NADAC as one connected descriptive-analysis revision.
6. Final cross-references, bibliography, layout, and whole-paper check.

Before marking a batch complete, check the author's saved edit against its
surrounding section and every affected summary passage. The shorter writing
sample remains deferred.
