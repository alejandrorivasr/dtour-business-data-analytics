# D Tour | Business Data Analytics

### An end-to-end operational and financial analytics case study

## Overview

This project originated from a real data analytics initiative at
D Tour, a family-owned educational field trip company in Tijuana,
Mexico.

The objective was to transform fragmented operational and
financial records into reliable information for business
decision-making.

The full internal project includes data cleaning, validation,
exploratory analysis, financial analysis, and business insights.

**Privacy notice:** Original business records and the full
internal notebooks are not publicly distributed.

## Business Questions

The internal analysis explored:

1. How has demand changed between school years?
2. Which destinations drive the most activity?
3. How does student participation vary by season?
4. How have revenue, expenses, and profitability evolved?
5. Which destinations have attractive estimated contribution
   margins?
6. How can data quality improve management decisions?

## Technical Approach

### Data Integration

Integrated operational records from historical Excel files
and Odoo exports into a consistent analytical structure.

### Data Quality

Investigated inconsistent classifications, duplicated records,
missing information, and services that did not take place.

Validation procedures were used to distinguish meaningful
business activity from administrative or incorrect records.

### Exploratory Analytics

Analyzed school-year demand, destination trends,
student participation, and seasonal variation.

### Financial Analytics

Examined accounting performance, transportation costs,
supplier expenses, and exploratory profitability scenarios.

### Business Interpretation

Translated analytical findings into operational and commercial
questions, while documenting data limitations and uncertainty.

## Public Reproducible Demonstration

This repository currently provides a small synthetic example
of the data integration and validation workflow.

The demonstration:

- Creates two fictional operational datasets.
- Standardizes different source schemas.
- Combines records into one dataset.
- Performs basic data quality checks.
- Excludes services flagged as not performed.
- Aggregates activity by school year.
- Generates a CSV summary and visualization.

**All demonstration records are fictional.**

The synthetic results do not reproduce or validate the
confidential financial findings of the internal project.

## Getting Started

Requires Python 3.10 or newer.

Clone this repository and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the demonstration:

```bash
python src/demo_pipeline.py
```

Generated files will appear in:

`reports/demo/`

## Public Repository Structure

```text
Dtour_DataScience_Public/
    README.md
    requirements.txt
    src/
        demo_pipeline.py
```

The original six analysis notebooks remain private.

## Technologies

- Python
- pandas
- NumPy (internal analysis)
- Matplotlib
- Jupyter Notebook (internal analysis)
- Excel
- Odoo

## Limitations

- Original data cannot be publicly released.
- The public demonstration uses synthetic records.
- The synthetic example is intentionally simplified.
- Full internal analysis results cannot be reproduced
  using the demonstration dataset.
- Project-level profitability scenarios are estimates,
  not independently verified financial margins.

## Next Improvements

- Add reusable validation functions.
- Add automated tests.
- Expand the synthetic demonstration to better illustrate
  the original analytical methods.
- Include a privacy-reviewed business case study.

## About

Developed as an applied data analytics project connecting
industrial engineering, business operations, and data science.

## Real Business Case Study

Read the [case study](CASE_STUDY.md) for the business problem, methodology, findings, and limitations.


## Selected Results from the Real Business

The following findings use aggregated internal business
data, not synthetic demonstration records.

- 1,129 integrated operational service records.
- 74 trips confirmed as not performed.
- Audited school-year trip volume declined by 15.80%.
- Reported January-June accounting profit declined
  by 22.48% between 2025 and 2026.

These figures reflect different comparison periods
and should not be interpreted as causal relationships.

### Audited Trip Volume

![Audited school-year trips](reports/figures/paseos_auditados.png)

### Student Participation

![Student participation](reports/figures/estudiantes_auditados.png)

### Destination Trends

![Destination changes](reports/figures/cambios_destinos_auditados.png)

### Financial Performance

![Semester financial comparison](reports/figures/comparacion_financiera_semestral.png)

For details, methodology and limitations, see
[CASE_STUDY.md](CASE_STUDY.md).


## Reproducing the Real Operational Analysis

Unlike the synthetic demo, this section uses real,
aggregated business data from the internal project.

The public datasets are:

- `data/aggregated/monthly_operations.csv`
- `data/aggregated/destination_operations.csv`

They contain aggregated trip and student counts,
without individual school or customer records.

### Run the analysis

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Reproduce the operational visualizations:

```bash
python src/reproduce_operational_analysis.py
```

This generates three charts in `reports/reproduced/`:

- School-year trip volumes
- Student participation by school year
- Destination-level changes

The datasets correspond to October-June comparisons
for the 2024-2025 and 2025-2026 school years.

Records confirmed as non-performed were excluded.

The public aggregated data reproduce the operational
results, but not the original cleaning process or
the private financial analysis.
