# Intäkt per stad

def intäkt_per_stad(df):
    return(
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending = False)
        )