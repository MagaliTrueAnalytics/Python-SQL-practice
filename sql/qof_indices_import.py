#creer la df
import pandas as pd

file = "quality_of_life_indices.csv"

df = pd.read_csv(file)
print(df.tail())

#voir les donnees
print(df.info())
print(df.describe(include = "all"))
#next : nettoyer au besoin et transferer via DB API connect & cursor()