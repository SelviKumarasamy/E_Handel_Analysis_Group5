#Load data from csv file

import pandas as pd

def load_data():
      df = pd.read_csv("data/ecommerce_sales.csv")
      return df   