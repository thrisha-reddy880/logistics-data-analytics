import matplotlib.pyplot as plt

def plot_shipping_days(df, output_path):
    plt.figure(figsize=(8, 5))
    df["Days for shipping (real)"].dropna().hist(bins=20)
    plt.title("Distribution of Actual Shipping Days")
    plt.xlabel("Actual Shipping Days")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

def plot_late_rate_by_shipping_mode(summary, output_path):
    plt.figure(figsize=(8, 5))
    plt.bar(summary["Shipping Mode"], summary["late_rate"])
    plt.title("Late Delivery Rate by Shipping Mode")
    plt.xlabel("Shipping Mode")
    plt.ylabel("Late Delivery Rate (%)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

def plot_orders_by_market(df, output_path):
    counts = df["Market"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(counts.index.astype(str), counts.values)
    plt.title("Orders by Market")
    plt.xlabel("Market")
    plt.ylabel("Number of Records")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
