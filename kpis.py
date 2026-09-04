import pandas as pd


def calculate_kpis(df):
    result = {}

    if "late_flag" in df.columns:
        result["Late Delivery Rate (%)"] = round(
            df["late_flag"].mean() * 100, 2
        )

    if "Days for shipping (real)" in df.columns:
        result["Average Actual Shipping Days"] = round(
            df["Days for shipping (real)"].mean(), 2
        )

    if "Days for shipment (scheduled)" in df.columns:
        result["Average Scheduled Shipping Days"] = round(
            df["Days for shipment (scheduled)"].mean(), 2
        )

    if "shipping_variance" in df.columns:
        result["Average Shipping Variance"] = round(
            df["shipping_variance"].mean(), 2
        )

    # DataCo uses "Order Id"
    if "Order Id" in df.columns:
        result["Unique Orders"] = int(df["Order Id"].nunique())

    return pd.DataFrame(
        [{"KPI": key, "Value": value} for key, value in result.items()]
    )


def shipping_mode_kpis(df):
    required = {
        "Shipping Mode",
        "Order Id",
        "Days for shipping (real)",
        "late_flag"
    }

    missing = required - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    result = (
        df.groupby("Shipping Mode")
        .agg(
            orders=("Order Id", "nunique"),
            avg_shipping_days=("Days for shipping (real)", "mean"),
            late_rate=("late_flag", "mean")
        )
        .reset_index()
    )

    result["avg_shipping_days"] = result["avg_shipping_days"].round(2)
    result["late_rate"] = (result["late_rate"] * 100).round(2)

    return result