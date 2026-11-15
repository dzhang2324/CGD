# Analysis and reproduction

Run `python -m analysis.run` from the repository root using Python 3.13 and
`requirements.txt`. Use `--output-dir PATH` to write a separate reproduction.
The pipeline does not execute the historical notebooks or scrape websites.

## Inputs and outputs

The source files are `data/raw/Medicaid_Spending_by_Drug_2021.csv` and
`data/raw/costplus.csv`. `data/reference/med_panel.csv` is a historical
transformation used to check the reconstruction, not the source of the new
Medicaid panel.

`analysis/output/` contains:

- `audit.json`: input hashes, dependency versions, filters, missingness,
  identifier checks, and comparisons with the historical panel.
- `estimates.csv` and `estimates.json`: full-precision estimates, standard
  errors, p-values, intervals, sample sizes, and percentage conversions.
- `drug_groups.csv`: numeric identifiers mapped to brand and generic names.
- `tables/`: generated regression and descriptive tables.
- `figures/`: generated plots.
- Other CSV files: the descriptive summaries and means used by the outputs.

Edit `analysis/report.py` to change generated tables or figures. The full paper
uses those outputs directly. `ShortPaper/` has independent copies to preserve
its content and layout.

## Medicaid

Observations are national drug-group/year records, not patients, states,
manufacturers, or individual claims. Groups are defined by the source pair
`(Brnd_Name, Gnrc_Name)`, which is not a product-strength or dosage-form
identifier. The source reports one manufacturer count per row, repeated
across 2017–2021.

Both log outcomes use the same sample: `Mftr_Name == "Overall"`,
`Outlier_Flag == 0`, and finite, positive manufacturer counts, spending,
dosage units, prescription claims, and both spending averages. Reshaping
preserves missing observations. The saved sample contains 12,740 observations
across 3,244 drug groups.

The primary outcome is the source's weighted spending per dosage unit; the
secondary outcome is spending per prescription claim. Each is regressed on
manufacturer count and year indicators, with and without log prescription
claims. OLS is unweighted. The omitted year is 2017.

There are no drug fixed effects because the reported manufacturer count is
constant within a drug group. Standard errors are clustered by the
brand/generic pair using the CR1 factor `G/(G-1) * (N-1)/(N-K)`; tests and
intervals use `t(G-1)`. The percentage association for one additional
manufacturer is `100 * expm1(beta)`, with interval endpoints transformed
the same way.

The estimates describe associations across drug groups. Manufacturer entry,
product mix, and prescription volume are not exogenous.

## Supplementary and historical results

Cost Plus uses the saved 442-row snapshot without re-scraping prices.
Estimated manufacturing cost is `(CP_price - 3) / 1.15`. The pipeline
preserves both historical log-log specifications with HC3 standard errors
and normal-reference inference.

Only the retail-price regression remains in the full paper. The markup
regression and additional plots remain reproducible historical outputs;
they are not retained manuscript results. Markup is calculated as
`100 * ((retail_price - 3) / estimated_cost - 1)`, so its relationship with
estimated cost is partly mechanical.

The missing `nadac_2019.csv` is not used by this pipeline. The full paper's
NADAC discussion retains historical descriptive results; those values have
not been newly reproduced. No NADAC analysis appears in the short paper.

## Verification

`python -m pytest -q` checks panel construction, missingness, sample filters,
group identifiers, audit failures, cost formulas, percentage conversions,
clustered covariance calculations, and HC3 calculations.

To validate a separate reproduction, compare its files with
`analysis/output/` under the pinned environment. The generated numerical
files and plots are deterministic; plot metadata excludes creation dates.
