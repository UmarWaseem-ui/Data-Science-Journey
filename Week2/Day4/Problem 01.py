# Student Dataset
# Create a CSV file named:
# students.csv

# with these columns:
    # Name
    # Age
    # Marks
# Add at least 6 students.

# Then:
    # Read the file.
    # Display the first 3 rows.
    # Display the last 2 rows.
    # Print the shape.
    # Print the column names.

import pandas as pd

# Read the file.
df=pd.read_csv("Students.csv")

# Display the first 3 rows.
print(df.head(3))

# Display the last 2 rows.
print(df.tail(2))

# Print the shape.
print(df.shape)

# Print the column names.
print(df.columns)