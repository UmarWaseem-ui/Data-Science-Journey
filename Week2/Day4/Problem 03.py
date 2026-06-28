# Personal Expense Dataset
# Create:
# Expenses.csv

# Columns:
    # Month
    # Food
    # Transport
    # Internet
# Add data for at least 6 months.

# Then:
    # Read the dataset.
    # Display the first 5 rows.
    # Display the last 3 rows.
    # Check the shape.
    # Print all column names.
    # Display the statistical summary using describe().

import pandas as pd

# Read the dataset.
df=pd.read_csv("Expense.csv")

# Display the first 5 rows.
print(df.head(5))

# Display the last 3 rows.
print(df.tail(3))

# Check the shape.
print(df.shape)

# Print all column names.
print(df.columns)

# Display the statistical summary using describe().
print(df.describe())