import matplotlib.pyplot as plt
import seaborn as sns

# Intäkt per stad

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

# Intäkt per katogori
def plot_intäkt_per_kategori(cat_rev):
    plt.bar(x = cat_rev.index, height = cat_rev.values)
    plt.xlabel("Kategori")
    plt.ylabel("Intäker(SEK)")  
    plt.title("Intäkter per Kategori")
    plt.show()

# Top Tre Kategori

def plot_top3_categories(top3):
    top3.plot(kind="bar", color="skyblue")
    plt.title("Top 3 produktkategorier efter intäkt")
    plt.xlabel("Produktkategorier")
    plt.ylabel("Total intäkt")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_intakt_stad_kategori(intakt_stad_kategori):
    """Visas total intäkt per kategori och stad i ett stapeldiagram."""

    intakt_stad_kategori.plot(
        kind="bar",
        figsize=(12, 6)
    )

    plt.title("Total intäkt per kategori och stad")
    plt.xlabel("Stad")
    plt.ylabel("Intäkt (kr)")
    plt.xticks(rotation=0)
    plt.legend(title="Kategori")
    plt.tight_layout()
    plt.show()    

# Skapa linjediagram över totala intäkter per vecka.


def plot_weekly_revenue_total(weekly_revenue_total):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data= weekly_revenue_total,
        x="date",
        y="revenue",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Intäkt per vecka [Total]")
    plt.title("Intäkt per vecka [Total], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weekly_revenue_mean(weekly_revenue_mean):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data= weekly_revenue_mean,
        x="date",
        y="revenue",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Intäkt per vecka [Genomsnitt]")
    plt.title("Intäkt per vecka [Genomsnitt], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def plot_weekly_revenue_median(weekly_revenue_median):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data= weekly_revenue_median,
        x="date",
        y="revenue",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Intäkt per vecka [Median]")
    plt.title("Intäkt per vecka [Median], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Skapa grafer över sålda enheter per vecka.

def plot_weekly_unit_total(weekly_units_total):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data = weekly_units_total,
        x="date",
        y="units",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Sålda enheter per vecka [Total]")
    plt.title("Sålda enheter per vecka [Total], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_weekly_unit_mean(weekly_units_mean):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data = weekly_units_mean,
        x="date",
        y="units",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Sålda enheter per vecka [Genomsnitt]")
    plt.title("Sålda enheter per vecka [Genomsnitt], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weekly_unit_median(weekly_units_median):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data = weekly_units_median,
        x="date",
        y="units",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Sålda enheter per vecka [Median]")
    plt.title("Sålda enheter per vecka [Median], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Skapa grafer över intäkt per vecka per kategori


def plot_weekly_total_revenue_by_category(weekly_total_revenue_by_category):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data = weekly_total_revenue_by_category,
        x="date",
        y="revenue",
        hue="category",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Total intäkt per vecka [Per kategori]")
    plt.title("Total intäkt per vecka [Per kategori], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_weekly_mean_revenue_by_category(weekly_mean_revenue_by_category):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data = weekly_mean_revenue_by_category,
        x="date",
        y="revenue",
        hue="category",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Total intäkt per vecka [Per kategori]")
    plt.title("Total intäkt per vecka [Per kategori], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_weekly_median_revenue_by_category(weekly_median_revenue_by_category):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data = weekly_median_revenue_by_category,
        x="date",
        y="revenue",
        hue="category",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Total intäkt per vecka [Per kategori]")
    plt.title("Total intäkt per vecka [Per kategori], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Skapa grafer över antalet sålda enheter per vecka per kategori


def plot_weekly_total_units_by_category(weekly_total_units_by_category):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=weekly_total_units_by_category,
        x="date",
        y="units",
        hue="category",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Totalt antal sålda enheter per vecka [Per kategori]")
    plt.title("Totalt antal sålda enheter per vecka [Per kategori], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weekly_mean_units_by_category(weekly_mean_units_by_category):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=weekly_mean_units_by_category,
        x="date",
        y="units",
        hue="category",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Genomsnittlig intäkt per vecka [Per enhet]")
    plt.title("Genomsnittlig intäkt per vecka [Per enhet], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  

def plot_weekly_median_units_by_category(weekly_median_units_by_category):
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=weekly_median_units_by_category,
        x="date",
        y="units",
        hue="category",
        marker="o"
    )

    plt.xlabel("Veckoslut")
    plt.ylabel("Median intäkt per vecka [Per enhet]")
    plt.title("Median intäkt per vecka [Per enhet], Januari–Juni 2024")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()




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
