# Week 3: Advanced Data Analysis and Visualization in Logistics

## Project overview
This project explores a **hypothetical/simulated logistics dataset** to demonstrate an end-to-end analytical workflow: data quality checks, exploratory data analysis, KPI calculations, group comparisons, correlation analysis, visualizations, and recommendations.

## Dataset
`data/hypothetical_logistics_dataset.csv` contains 2,400 simulated orders and fields for order date, actual and scheduled delivery days, shipping mode, distance, freight cost, quantity, customer segment, region, and delivery status. The dataset is synthetic and must not be represented as real company data.

## Run the analysis (Windows)
```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python src\logistics_analysis.py
```
Outputs are written to `outputs/`.

## Main outputs
- `kpi_summary.csv`
- `descriptive_statistics.csv`
- `correlation_matrix.csv`
- `shipping_mode_analysis.csv`
- `customer_segment_analysis.csv`
- `regional_analysis.csv`
- six PNG charts
- `analysis_summary.txt`

## Methodology
1. Parse dates and convert numeric columns.
2. Impute missing numeric values with the median and categorical values with the mode.
3. Remove duplicate rows.
4. Recalculate late/on-time status from actual versus scheduled delivery days.
5. Calculate central tendency, distribution summaries, delivery KPIs, group comparisons, and Pearson correlations.
6. Visualize distribution, category differences, relationships, and monthly volume.

## Important note
This is a teaching/demo project built with simulated data. If your internship supervisor expects continuity with Weeks 1–2, replace the input CSV with your approved cleaned dataset and adapt the column names in `src/logistics_analysis.py`. Never upload confidential raw data.

