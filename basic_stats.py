import pandas as pd

print("Loading dataset...")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

print("First 5 rows:")
print(data.head())

print("\nDataset Info:")


print("\nStatistical Summary:")
print(data.describe())
