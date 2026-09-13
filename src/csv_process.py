import pandas as pd
from datetime import datetime

df = pd.read_csv("../data/raw/ai4i2020.csv")

df = df.drop(columns=["TWF","HDF","PWF","OSF","RNF"])
timest = datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_csv(f"../data/processed/data_wo_cols_{timest}.csv")
