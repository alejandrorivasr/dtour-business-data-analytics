# Case Study: Turning Business Records into Actionable Insights

## 1. Business Context

D Tour is a family-owned company specializing in educational
field trips in Tijuana, Mexico.

The company manages trip scheduling, school relationships,
transportation coordination, destination suppliers, and
financial operations.

Over time, operational information accumulated across
historical spreadsheets and Odoo exports.

This created an opportunity to improve data reliability
and develop a more consistent analytical process.

## 2. The Problem

The original information presented several challenges:

- Multiple data sources with different structures.
- Inconsistent service classifications.
- Administrative records mixed with actual services.
- Services recorded despite not taking place.
- Incomplete connections between operational and sales data.
- Differences between accounting dates and service dates.

These issues complicated comparisons of business performance
across periods.

## 3. Analytical Approach

### Data Auditing

Explored the original datasets, reviewed column structures,
investigated missing values, and identified questionable records.

### Data Cleaning and Integration

Standardized dates, service categories, and destination names.

Integrated historical Excel records with Odoo operational data.

### Data Validation

Introduced consistency checks and compared processed datasets
to identify unexpected differences.

Confirmed cancellations and non-performed services were
flagged explicitly rather than silently discarded.

### Operational Analysis

Compared educational trip activity across school years.

Investigated participation trends, destination performance,
and monthly seasonality.

### Financial Analysis

Analyzed revenues, operating expenses, accounting profit,
and changes in profit margins between comparable periods.

Developed exploratory destination profitability scenarios
using linked sales and historical cost approximations.

## 4. Key Findings


### Quantitative Findings from the Real Business

**Data quality and operational performance**

The integrated operational dataset contained 1,129 service
records. Following a detailed audit, 74 trip records were
confirmed as services that had not taken place.

For the comparable October-June periods:

| Metric | 2024-2025 | 2025-2026 | Change |
|---|---:|---:|---:|
| Audited trips | 386 | 325 | -15.80% |
| Student participations | 51,017 | 42,051 | -17.57% |

Before the final audit, the preliminary comparison suggested
a 28.82% decline in trips. After correcting the records,
the audited decline was 15.80%.

This substantially changed the interpretation of the
company's operational performance.

**Destination availability sensitivity**

Two destinations were affected by external restrictions
or temporary unavailability.

When these destinations and related packages were excluded,
the comparison showed:

- Trip volume: -7.16%
- Student participation: -9.51%

This sensitivity analysis is descriptive and does not
establish that the restrictions caused the entire difference.

**Financial performance**

Accounting results for January-June:

| Metric (MXN) | 2025 | 2026 |
|---|---:|---:|
| Revenue | 5,348,173 | 4,178,743 |
| Expenses | 3,754,182 | 2,943,105 |
| Accounting profit | 1,593,991 | 1,235,638 |
| Profit margin | 29.80% | 29.57% |

Revenue declined by 21.87%, while reported accounting
profit declined by 22.48%.

The accounting profit margin remained relatively stable.

These comparisons assume that the semester-level expense
records are complete. Individual monthly expense dates
may not correspond to service dates.

**Exploratory destination contribution margins**

Under the baseline historical-cost assumptions:

- El Trompo: 41.25%
- CECUT: 37.69%
- Mictlan: 35.69%
- Ruta del Maiz: 34.86%
- Casian: 29.19%
- Cine: 26.59%

These are illustrative scenarios using estimated supplier
costs and standard transportation costs. They are NOT
verified actual margins or audited net profit.

The underlying sales matching was incomplete and included
name-based project matching.


### Data Quality Changed the Business Interpretation

Cleaning and auditing the records materially changed the
interpretation of historical business activity.

This demonstrated why validating operational definitions
is necessary before drawing conclusions from business KPIs.

### Destination Availability Matters

Some destinations were affected by external operating
restrictions or temporary unavailability.

A sensitivity analysis helped distinguish overall changes
in activity from changes associated with those destinations.

This analysis was descriptive and did not establish
causal effects.

### Revenue and Profit Must Be Evaluated Together

Financial analysis showed that changes in revenue and
absolute profit can occur while accounting profit margins
remain relatively stable.

This highlighted the value of considering both growth
and profitability in management reporting.

### Revenue Is Not the Same as Profitability

High-revenue destinations were not necessarily those
with the highest estimated contribution margins.

Cost-allocation uncertainty prevented the analysis
from establishing definitive profitability rankings.

## 5. Business Applications

The findings provide a foundation for:

- Monitoring performance with consistent definitions.
- Evaluating destination offerings using contribution
  rather than revenue alone.
- Identifying opportunities to recover school demand.
- Improving the collection of project-level cost data.
- Supporting more targeted commercial campaigns.
- Establishing repeatable management reporting.

These are potential applications, not measured financial
improvements attributable to the project.

## 6. Technical Skills Demonstrated

- Data inspection and quality assessment.
- Integration of heterogeneous business sources.
- Data cleaning and transformation with pandas.
- Reproducible validation checks.
- Exploratory data analysis.
- Financial performance comparisons.
- Sensitivity analysis.
- Data visualization.
- Interpretation of analytical limitations.

## 7. Limitations

The original business datasets and internal notebooks
are confidential and are not publicly distributed.

The public Python demonstration contains only fictional
records and does not reproduce the real financial analysis.

Some historical identifiers changed during processing,
although a comparison verified equivalence for the
selected analytical fields.

Sales-to-project matching was incomplete and based partly
on normalized project names.

Historical supplier costs could not always be reliably
assigned to individual services.

The destination margin estimates therefore represent
exploratory scenarios, not audited profitability.

## 8. Conclusion

The most important contribution of this project was
not a predictive model.

It was the development of a more reliable analytical
foundation for a real business.

The project illustrates how data engineering, quality
validation, business analytics, and careful interpretation
can support better management decisions.
