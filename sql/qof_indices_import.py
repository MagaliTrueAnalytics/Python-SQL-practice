import pandas as pd

file = "quality_of_life_indices.csv"

df = pd.read_csv(file)
print(df.tail(10))
