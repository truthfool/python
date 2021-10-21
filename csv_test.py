import pandas as pd

df = pd.read_csv("complaints.csv")

print(df.head(5000).to_csv("export-5k-rows.csv"))