from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_customer_cities(df, n_clusters=4):
    required = {
        "Customer City",
        "Order ID",
        "Order Item Total",
        "Order Item Quantity",
        "late_flag"
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    grouped = (
        df.groupby("Customer City")
        .agg(
            order_count=("Order ID", "nunique"),
            avg_order_value=("Order Item Total", "mean"),
            avg_quantity=("Order Item Quantity", "mean"),
            late_rate=("late_flag", "mean")
        )
        .dropna()
    )

    scaler = StandardScaler()
    X = scaler.fit_transform(grouped)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    grouped["segment"] = model.fit_predict(X)

    return grouped, model
