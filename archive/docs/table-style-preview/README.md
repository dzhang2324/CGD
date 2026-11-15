# Table presentation preview

This standalone illustration does not change `Paper/main.tex`, generated
regression tables, or analysis code. Coefficients, standard errors, sample
sizes, controls, and fit statistics are copied from the current dosage-unit
table. The covariate table is a short style sample, not a complete replacement
for the manuscript's data dictionary.

Published example:

Brückner, Markus, and Antonio Ciccone. 2011. “Rain and the Democratic
Window of Opportunity.” *Econometrica* 79(3): 923–947.

- Regression results: Table III, printed page 932, PDF page 10.
- Covariate definitions: Table I, printed page 929, PDF page 7.
- Summary statistics: Table II, printed page 930, PDF page 8.
- Published PDF: https://crei.cat/wp-content/uploads/2016/07/RDW-pub.pdf
- DOI: https://doi.org/10.3982/ECTA8183

Conventions illustrated: numbered specifications, outcome headings,
coefficients with standard errors beneath, readable covariate labels,
light horizontal rules, no vertical grid, and notes below the table.
Table III in the example has no R-squared row; the preview retains both fit
statistics from the current thesis table.

Compile with:

```sh
tectonic --only-cached preview.tex
```
