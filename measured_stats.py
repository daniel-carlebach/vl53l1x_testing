import pandas as pd

df = pd.read_csv("data/coffee_table_415_mm.csv")

print(df["Distance (mm)"].describe())