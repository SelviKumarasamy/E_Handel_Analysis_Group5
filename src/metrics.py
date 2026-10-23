# Intäkt per stad

def intäkt_per_stad(df):
     return(
        df.groupby("city")["revenue"]
        .sum()
        .sort_values(ascending = False)
    )


def ordervarden(df):
    return df.groupby("order_id")["revenue"].sum()
