#Load data from csv file


import pandas as pd
from pathlib import Path

def load_data():
    """Läser in e-handelsdata"""

    df = pd.read_csv("data/ecommerce_sales.csv")

    return df
