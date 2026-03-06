import pandas as pd
import numpy as np

data = {
    "Age": [25, np.nan, 30, 22, np.nan],
    "Salary": [50000, 60000, np.nan, 45000, 52000],
    "Department": ["HR", "IT", None, "Finance", "IT"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nMissing values (True = Missing):")
print(df.isnull())

# Missing values per column
print("\nMissing values per column:")
print(df.isnull().sum())

# Total missing values in the whole dataset
total_missing = df.isnull().sum().sum()
print("\nTotal missing values in dataset:", total_missing)