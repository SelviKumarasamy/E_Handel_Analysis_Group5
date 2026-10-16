import pandas as pd


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
