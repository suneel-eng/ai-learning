# Most real-world data is incomplete, inconsistent, or noisy.
# Cleaning and preprocessing ensures your model learns from quality data, not garbage.

# Example dataset
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "Name": ["Simhadri", "Arjun", None, None, "Simhadri", "Kavya", "Renu"],
    "Score": [95, None, 88, None, 95, 100, 25],
    "Passed": ["Yes", "No", "Yes", None, "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)
print(df)

# Cleaning steps
# 1. Handle missing values
df.dropna(inplace=True)           # Remove rows with missing values
print(df)
df.fillna("Unknown", inplace=True)  # Replace missing with default
print(df)
df["Score"].fillna(df["Score"].mean(), inplace=True)  # Fill with mean
print(df)

# 2. Remove duplicates
df.drop_duplicates(inplace=True)
print(df)

# 3. Type conversion
print(df.dtypes)
df["Score"] = df["Score"].astype(int)
print(df.dtypes)

# 4. Encoding categorical data
df["Passed"] = df["Passed"].map({"Yes": 1, "No": 0})
print(df)

# 5. Normalization (Scaling)
scaler = MinMaxScaler()
df["Score"] = scaler.fit_transform(df[["Score"]])
print(df)