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