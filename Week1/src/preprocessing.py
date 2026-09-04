import pandas as pd

ORDER_DATE = "order date (DateOrders)"
SHIPPING_DATE = "shipping date (DateOrders)"

def clean_and_engineer(df):
    df = df.copy()

    for col in [ORDER_DATE, SHIPPING_DATE]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    if {
        "Days for shipping (real)",
        "Days for shipment (scheduled)"
    }.issubset(df.columns):
        df["shipping_variance"] = (
            df["Days for shipping (real)"]
            - df["Days for shipment (scheduled)"]
        )
        df["late_flag"] = (df["shipping_variance"] > 0).astype(int)

    if ORDER_DATE in df.columns:
        df["order_month"] = df[ORDER_DATE].dt.to_period("M").astype(str)
        df["order_day_of_week"] = df[ORDER_DATE].dt.day_name()

    return df
