#Loading the data

import pandas as pd

def load_data("data/ecommerce_sales.csv"): 
     return pd.read.csv("data/ecommerce_sales.csv")
