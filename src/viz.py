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


def plot_intakt_per_stad(stads_intäkt):
    stads_intäkt.sort_values().plot(
        kind="barh",
        figsize=(9, 5)
    )

    plt.title("Total intäkt per stad")
    plt.xlabel("Intäkt (kr)")
    plt.ylabel("Stad")
    plt.tight_layout()
    plt.show()

 
def plot_ordervarden(order_values):

    plt.figure(figsize=(9, 5))

    plt.hist(order_values, bins=20, edgecolor="black")

    plt.title("Fördelning av ordervärden")
    plt.xlabel("Ordervärde (kr)")
    plt.ylabel("Antal order")
    plt.tight_layout()
    plt.show()
