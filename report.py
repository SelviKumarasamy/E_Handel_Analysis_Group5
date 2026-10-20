import pandas as pd
df = pd.read_csv("data/ecommerce_sales.csv")
print (df.head())
print (df.columns)
print (df.groupby ("category")["revenue"].sum().sort_values(ascending=False))