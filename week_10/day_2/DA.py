# Import necessary libraries
import pandas as pd
import numpy as np

# Creating a Series by passing a list of values, letting pandas create a default RangeIndex
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# Creating a date range
dates = pd.date_range("20230101", periods=6)
print(dates)

# Creating a DataFrame with random data
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# np.random.randn(6, 4) generates random numbers from a standard normal distribution (mean=0, standard deviation=1) in a 6x4 array.
# 'index=dates' specifies the index (row labels) of the DataFrame.
# 'columns=list("ABCD")' creates columns named 'A', 'B', 'C', and 'D'.
print(df)

# Display the first 2 rows of the DataFrame
print(df.head(2))  # When you call df.head(), it will return the first 5 rows (by default) of your DataFrame

# Display the last 2 rows of the DataFrame
print(df.tail(2))

# Print the index of the DataFrame
print(df.index)

# Print the column names of the DataFrame
print(df.columns)

# Convert the DataFrame to a NumPy array
print(df.to_numpy())  # Return a NumPy representation of the data without the index or column label

# Display summary statistics of the DataFrame
print(df.describe())  # Shows a quick statistic summary of your data

# Print data types of each column in the DataFrame
print(df.dtypes)

# Transpose the data
print(df.T)

# Sort the columns of the DataFrame 'df' in descending order
print(df.sort_index(axis=1, ascending=False))
# axis=0: Sorting along the rows, and axis=1: Sorting along the columns

# Sort the rows of the DataFrame in descending order
print(df.sort_index(axis=0, ascending=False))

# Sort the DataFrame based on the values in column 'B' in ascending order
print(df.sort_values(by="B"))

# Select column 'A'
print(df["A"])

# Select the first 3 rows
print(df[0:3])

# Slice the DataFrame by date range
print(df["20230103":"20230104"])

# Selection by label for the first date
print(df.loc[dates[0]])

# Label-based slicing, including both endpoints
print(df.loc["20230102":"20230104"], ["A", "B"])

# Select the data at position 3 (4th row)
print(df.iloc[3])

# Select rows where values in column 'A' are greater than 0
print(df[df["A"] > 0])

# Create a copy of the DataFrame and add a new column 'E'
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
