# Pandas makes it easy to load, clean, explore, and transform data.
# Essential steps before feeding it into any AI model.

# Pandas is a Python library for working with tabular data — like spreadsheets or CSV files.
import pandas as pd

# Creating a DataFrame
# Think of a DataFrame as an Excel sheet in Python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)
print(df)

# Loading Data from a CSV file
df = pd.read_csv('students.csv')
print(df)

print(df.head())  # Display the first 5 rows
print(df.tail())  # Display the last 5 rows
print(df.shape) # Get the number of rows and columns
print(df.info()) # Get a summary of the DataFrame
print(df.describe()) # Get basic statistics for numerical columns

# Data Cleaning
df.dropna()           # Remove missing rows
df.fillna(0)          # Replace missing values with 0
df["Class"] = df["Class"].astype(int)  # Convert type
