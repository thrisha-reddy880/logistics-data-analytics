"""
Week 1 Logistics Strategic Planning and Data Exploration

Run from the project root:
    python notebooks/01_week1_exploration.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import load_data, profile_data
from src.preprocessing import clean_and_engineer
from src.kpis import calculate_kpis, shipping_mode_kpis
from src.eda import (
    plot_shipping_days,
    plot_late_rate_by_shipping_mode,
    plot_orders_by_market
)
from src.config import OUTPUT_DIR

print("=" * 70)
print("WEEK 1 - LOGISTICS DATA EXPLORATION")
print("=" * 70)

df = load_data()

profile = profile_data(df)

print(f"Rows: {profile['rows']:,}")
print(f"Columns: {profile['columns']}")
print(f"Duplicate rows: {profile['duplicate_rows']}")

print("\nTop missing-value columns:")
print(profile["missing_values"].head(10))

df = clean_and_engineer(df)

print("\nKPI SUMMARY")
print(calculate_kpis(df))

kpi_table = calculate_kpis(df)
kpi_table.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)

print("\nSHIPPING MODE ANALYSIS")
shipping_summary = shipping_mode_kpis(df)
print(shipping_summary)

shipping_summary.to_csv(
    OUTPUT_DIR / "shipping_mode_analysis.csv",
    index=False
)

if "Days for shipping (real)" in df.columns:
    plot_shipping_days(
        df,
        OUTPUT_DIR / "shipping_days_distribution.png"
    )

if not shipping_summary.empty:
    plot_late_rate_by_shipping_mode(
        shipping_summary,
        OUTPUT_DIR / "late_rate_by_shipping_mode.png"
    )

if "Market" in df.columns:
    plot_orders_by_market(
        df,
        OUTPUT_DIR / "orders_by_market.png"
    )

print("\nAnalysis complete. Check the outputs/ folder.")
