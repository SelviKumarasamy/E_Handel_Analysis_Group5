import matplotlib.pyplot as plt

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