# Employee Dataset
# Create:
# employees.csv

# Columns:
    # Employee ID
    # Name
    # Department
    # Salary
# Add 8 employees.

# Then:
    # Read the dataset.
    # Use info().
    # Use describe().
    # Print the number of rows and columns.

import pandas as pd

# Read the dataset.
df=pd.read_csv("Employees.csv")

# Use info().
print(df.info())

# Use Describe
print(df.describe())

# Print the number of Rows and Columns
print(df.shape)