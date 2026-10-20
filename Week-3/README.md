# Week 3 — Logistics Data Exploration and Visualization

**Dataset source:** Week 2 simulated logistics dataset in this repository.  
**GitHub repository:** https://github.com/thrisha-reddy880/logistics-data-analytics  
**Dataset file:** `data/logistics_data_raw.csv`

## Objective
Perform exploratory data analysis (EDA) on delivery time, shipping mode, route distance, freight cost, quantity, customer segment, and recorded delivery status. The project includes data validation, descriptive statistics, six charts, a written report, and reproducible Python code.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run: `python src/logistics_analysis.py`
5. Review CSV/JSON outputs in `outputs/` and charts in `outputs/charts/`.

## Data quality choices
- Duplicate `Order_ID` rows are removed by keeping the first record.
- Category labels are trimmed and shipping-mode capitalization is standardized.
- Non-positive delivery days, distance, and freight cost are marked missing because they are not valid physical measurements.
- IQR outliers are flagged for review and retained rather than automatically deleted or capped.
- Missing values are reported; no unsupported values are imputed.

## Charts
1. Delivery-time histogram — distribution and skew.
2. Average freight cost by shipping mode — cost comparison.
3. Delivery-time box plot by shipping mode — median, spread, and potential outliers.
4. Distance-versus-freight scatter plot — relationship between route length and cost.
5. Delivery-status count plot — operational status mix.
6. Correlation heatmap — linear association among numeric variables.

## Important limitation
This is a small simulated teaching dataset (60 distinct orders after duplicate removal). Findings are descriptive and should not be generalized to a real logistics operation without a larger, representative dataset and additional fields such as promised delivery date, carrier, origin/destination, and fuel surcharge.

