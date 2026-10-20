from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "logistics_data_raw.csv"
OUT = ROOT / "outputs"
CHARTS = OUT / "charts"
OUT.mkdir(exist_ok=True)
CHARTS.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid", context="notebook")

raw = pd.read_csv(DATA)
raw_rows = len(raw)
duplicate_rows = int(raw.duplicated(subset=["Order_ID"]).sum())

df = raw.drop_duplicates(subset=["Order_ID"], keep="first").copy()
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
numeric = ["Delivery_Days", "Distance_km", "Freight_Cost", "Quantity"]
for col in numeric:
    df[col] = pd.to_numeric(df[col], errors="coerce")
for col in ["Shipping_Mode", "Customer_Segment", "Delivery_Status"]:
    df[col] = df[col].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
df["Shipping_Mode"] = df["Shipping_Mode"].str.title()
df["Customer_Segment"] = df["Customer_Segment"].str.title()
df["Delivery_Status"] = df["Delivery_Status"].str.strip()

# Impossible physical measurements are treated as missing, not silently corrected.
invalid_delivery = int((df["Delivery_Days"] <= 0).sum())
invalid_distance = int((df["Distance_km"] <= 0).sum())
invalid_cost = int((df["Freight_Cost"] <= 0).sum())
df.loc[df["Delivery_Days"] <= 0, "Delivery_Days"] = float("nan")
df.loc[df["Distance_km"] <= 0, "Distance_km"] = float("nan")
df.loc[df["Freight_Cost"] <= 0, "Freight_Cost"] = float("nan")

# Outliers are flagged for investigation; retained in cleaned file for traceability.
outlier_flags = {}
for col in ["Delivery_Days", "Distance_km", "Freight_Cost"]:
    s = df[col].dropna()
    q1, q3 = s.quantile(.25), s.quantile(.75)
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    flag = (df[col] < low) | (df[col] > high)
    outlier_flags[col] = int(flag.sum())
    df[f"{col}_Outlier_Flag"] = flag.fillna(False)

df.to_csv(OUT / "cleaned_logistics_data.csv", index=False)
df[numeric].describe().T.to_csv(OUT / "numeric_summary.csv")
df.groupby("Shipping_Mode", dropna=False).agg(
    Orders=("Order_ID", "count"),
    Mean_Delivery_Days=("Delivery_Days", "mean"),
    Median_Delivery_Days=("Delivery_Days", "median"),
    Mean_Freight_Cost=("Freight_Cost", "mean"),
    Median_Freight_Cost=("Freight_Cost", "median"),
    Mean_Distance_km=("Distance_km", "mean")
).round(2).to_csv(OUT / "shipping_mode_summary.csv")
df["Delivery_Status"].value_counts(dropna=False).rename_axis("Delivery_Status").reset_index(name="Orders").to_csv(OUT / "status_summary.csv", index=False)
df[numeric].corr().round(3).to_csv(OUT / "correlation_matrix.csv")
df.isna().sum().rename("Missing_Count").to_csv(OUT / "missing_values_after_validation.csv")

# Six charts, each chosen to answer a specific analytical question.
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Delivery_Days", bins=12, kde=True, color="#3676a8")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery days"); plt.ylabel("Order count"); plt.tight_layout()
plt.savefig(CHARTS / "delivery_days_distribution.png", dpi=180); plt.close()

mode_cost = df.groupby("Shipping_Mode", as_index=False)["Freight_Cost"].mean().sort_values("Freight_Cost")
plt.figure(figsize=(8, 5))
sns.barplot(data=mode_cost, x="Shipping_Mode", y="Freight_Cost", color="#4c9a8a")
plt.title("Average Freight Cost by Shipping Mode")
plt.xlabel("Shipping mode"); plt.ylabel("Average freight cost"); plt.xticks(rotation=15)
plt.tight_layout(); plt.savefig(CHARTS / "freight_cost_by_mode.png", dpi=180); plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Shipping_Mode", y="Delivery_Days", color="#88b6d9")
plt.title("Delivery-Time Spread by Shipping Mode")
plt.xlabel("Shipping mode"); plt.ylabel("Delivery days"); plt.xticks(rotation=15)
plt.tight_layout(); plt.savefig(CHARTS / "delivery_days_by_mode.png", dpi=180); plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Distance_km", y="Freight_Cost", hue="Shipping_Mode", s=75)
plt.title("Distance vs Freight Cost")
plt.xlabel("Distance (km)"); plt.ylabel("Freight cost"); plt.tight_layout()
plt.savefig(CHARTS / "distance_vs_freight.png", dpi=180); plt.close()

status_order = df["Delivery_Status"].value_counts().index
plt.figure(figsize=(8, 5))
sns.countplot(data=df, y="Delivery_Status", order=status_order, color="#d39b54")
plt.title("Orders by Recorded Delivery Status")
plt.xlabel("Order count"); plt.ylabel("Delivery status"); plt.tight_layout()
plt.savefig(CHARTS / "delivery_status_counts.png", dpi=180); plt.close()

corr = df[numeric].corr()
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap="vlag", center=0, fmt=".2f", square=True)
plt.title("Correlation Between Numeric Variables")
plt.tight_layout(); plt.savefig(CHARTS / "correlation_heatmap.png", dpi=180); plt.close()

valid_days = df["Delivery_Days"].dropna()
valid_cost = df["Freight_Cost"].dropna()
status_counts = df["Delivery_Status"].value_counts().to_dict()
mode_stats = df.groupby("Shipping_Mode").agg(
    orders=("Order_ID", "count"),
    avg_days=("Delivery_Days", "mean"),
    median_days=("Delivery_Days", "median"),
    avg_cost=("Freight_Cost", "mean"),
    avg_distance=("Distance_km", "mean")
).round(2)
summary = {
    "raw_rows": raw_rows,
    "unique_orders_after_deduplication": int(df["Order_ID"].nunique()),
    "duplicate_rows_removed": duplicate_rows,
    "missing_values_in_raw": {k: int(v) for k, v in raw.isna().sum().items() if v},
    "invalid_values_changed_to_missing": {
        "nonpositive_delivery_days": invalid_delivery,
        "nonpositive_distance_km": invalid_distance,
        "nonpositive_freight_cost": invalid_cost
    },
    "outlier_flags_iqr": outlier_flags,
    "delivery_days": {
        "count": int(valid_days.count()),
        "mean": round(float(valid_days.mean()), 2),
        "median": round(float(valid_days.median()), 2),
        "std": round(float(valid_days.std()), 2),
        "min": round(float(valid_days.min()), 2),
        "max": round(float(valid_days.max()), 2)
    },
    "freight_cost": {
        "count": int(valid_cost.count()),
        "mean": round(float(valid_cost.mean()), 2),
        "median": round(float(valid_cost.median()), 2),
        "min": round(float(valid_cost.min()), 2),
        "max": round(float(valid_cost.max()), 2)
    },
    "status_counts": {str(k): int(v) for k, v in status_counts.items()},
    "shipping_mode_summary": mode_stats.to_dict(orient="index"),
    "correlations": corr.round(3).to_dict()
}
(OUT / "analysis_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))
