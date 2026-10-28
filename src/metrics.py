import pandas as pd
import numpy as np


#  Total Intäkt och Antal enheter function 
def total(rev, unit):
    return rev.astype(int).sum(), unit.sum()


def compute_aov(df: pd.DataFrame) -> float:
    """Average Order Value: total intäkt delat med antal ordrar."""
    return df["revenue"].sum() / df["order_id"].nunique()


def order_value_spread(df: pd.DataFrame) -> pd.Series:
    """Spridningsmått för ordervärde."""
    revenue = df["revenue"]
    return pd.Series({
        "AOV (medel)": compute_aov(df),
        "Median": revenue.median(),
        "Std": revenue.std(),
        "Min": revenue.min(),
        "25 %": revenue.quantile(0.25),
        "75 %": revenue.quantile(0.75),
        "Max": revenue.max(),
    }).round(2)


# Intäkt per stad

def intäkt_per_stad(df):
     return(
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending = False)
    )

# Intäk per kategori
def intäkt_per_kategori(df):
     return(
          df.groupby("category")["revenue"].sum()
          .sort_values(ascending = False)
     )     

def ordervarden(df):
    return df.groupby("order_id")["revenue"].sum()


def hitta_avvikelser(df, kolumner = None):

    if kolumner is None:    
     kolumner = ["price", "units", "revenue"]

    sammanfattningar = []
    outlier_limit = {}
    outlier_data = {}

    for kolumn in kolumner:
     values = df[kolumn].dropna().to_numpy()

    minimum = np.min(values)
    q1 = np.percentile(values, 25)
    median = np.median(values)
    q3 = np.percentile(values, 75)
    maximum = np.max(values)

    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    # Identifiera potentiella avvikande värden
    mask = (df[kolumn] < lower_limit) | (
        df[kolumn] > upper_limit
    )
    avvikelser = df.loc[mask]

    sammanfattningar.append({
        "Kolumn": kolumn,
        "Minimum": minimum,
        "Q1": q1,
        "Median": median,
        "Q3": q3,
        "Maximum": maximum,
        "IQR": iqr,
        "Antal avvikelser": len(avvikelser)
    })

    outlier_limit[kolumn] = (
        lower_limit, upper_limit
    )
    outlier_data[kolumn] = avvikelser

    sammanfattning = pd.DataFrame(sammanfattningar)
    return sammanfattning, outlier_limit, outlier_data

def unika_avvikelser(outlier_data):
     alla_avvikelser = pd.concat(outlier_data.values()).drop_duplicates()

     print(f"Totalt antal unika rader med avvikelser: {len(alla_avvikelser)}")

     return(
     alla_avvikelser.sort_values("revenue", ascending=False)
     )


# Följande funktion räknar ut den totala intäkten per tidsenhet
def total_revenue(data, frequency):
    result = (
        data.groupby(pd.Grouper(key="date", freq=frequency))["revenue"]
        .sum()
        .reset_index()
    )
    return result



# Följande funktion räknar ut den totala intäkten per tidsenhet
def mean_revenue(data, frequency):
    result = (
        data.groupby(pd.Grouper(key="date", freq=frequency))["revenue"]
        .mean()
        .reset_index()
    )
    return result



# Följande funktion räknar ut den totala intäkten per tidsenhet
def median_revenue(data, frequency):
    result = (
        data.groupby(pd.Grouper(key="date", freq=frequency))["revenue"]
        .median()
        .reset_index()
    )
    return result



# Funktioner för antalet enheter
def total_units(data, frequency):
    result = (
        data.groupby(pd.Grouper(key="date", freq=frequency))["units"]
        .sum()
        .reset_index()
    )
    return result



# # Funktioner för antalet enheter
def mean_units(data, frequency):
    result = (
        data.groupby(pd.Grouper(key="date", freq=frequency))["units"]
        .mean()
        .reset_index()
    )
    return result


# Funktioner för antalet enheter
def median_units(data, frequency):
    result = (
        data.groupby(pd.Grouper(key="date", freq=frequency))["units"]
        .median()
        .reset_index()
    )
    return result



# Funktion för intäkt per kategori och tidsperiod
def total_revenue_by_category(data, frequency):
    result = (
        data.groupby(["category", pd.Grouper(key="date", freq=frequency)])["revenue"]
        .sum()
        .reset_index()
    )
    return result



# Funktion för intäkt per kategori och tidsperiod
def mean_revenue_by_category(data, frequency):
    result = (
        data.groupby(["category", pd.Grouper(key="date", freq=frequency)])["revenue"]
        .mean()
        .reset_index()
    )
    return result



# Funktion för intäkt per kategori och tidsperiod
def median_revenue_by_category(data, frequency):
    result = (
        data.groupby(["category", pd.Grouper(key="date", freq=frequency)])["revenue"]
        .median()
        .reset_index()
    )
    return result



##
# Följande funktion räknar ut antalet sålda enhehter per kategori och tidsperiod
def total_units_by_category(data, frequency):
    result = (
        data.groupby(["category", pd.Grouper(key="date", freq=frequency)])["units"]
        .sum()
        .reset_index()
    )
    return result



# Följande funktion räknar ut antalet sålda enhehter per kategori och tidsperiod
def mean_units_by_category(data, frequency):
    result = (
        data.groupby(["category", pd.Grouper(key="date", freq=frequency)])["units"]
        .mean()
        .reset_index()
    )
    return result


# Följande funktion räknar ut antalet sålda enhehter per kategori och tidsperiod
def median_units_by_category(data, frequency):
    result = (
        data.groupby(["category", pd.Grouper(key="date", freq=frequency)])["units"]
        .median()
        .reset_index()
    )
    return result

