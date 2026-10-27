import pandas as pd
import matplotib.pyplot as plt
df = pd.read_csv("data/ecommerce_sales.csv")
top3 = df.groupby("category")["revenue"].sum().nlargest(3)
print(top3)
top3.plot(kind="bar",title="Top 3 categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()