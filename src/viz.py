import matplotlib.pyplot as plt


def plot_order_value_distribution(df):
    """Histogram över ordervärde med medel (AOV) och median markerade."""
    revenue = df["revenue"]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(revenue, bins=40, color="steelblue", edgecolor="white")
    ax.axvline(revenue.mean(), color="red", linestyle="--",
               label=f"Medel (AOV): {revenue.mean():.0f} kr")
    ax.axvline(revenue.median(), color="black", linestyle=":",
               label=f"Median: {revenue.median():.0f} kr")
    ax.set_title("Fördelning av ordervärde")
    ax.set_xlabel("Ordervärde (kr)")
    ax.set_ylabel("Antal ordrar")
    ax.legend()
    plt.show()
