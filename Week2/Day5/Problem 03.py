# Missing Values
# Create the following DataFrame:

# Name	    Age	    Marks
# Ali	    20	    85
# Ahmed	    NaN	    90
# Umar	    19	    NaN
# Sara	    24	    95
# Ayesha	NaN	    88

# Then:
    # Display all missing values using isnull().
    # Count the missing values in each column using isnull().sum().
    # Create a new DataFrame after removing missing values with dropna().
    # Fill the missing values with 0 using fillna(0).
    # Fill the missing values in the Age column with the average age.

import pandas as pd
import numpy as np

Data = {
    'Name': ['Ali', 'Ahmed', 'Umar', 'Sara', 'Ayesha'],
    'Age': [20, np.nan, 19, 24, np.nan],
    'Marks': [85, 90, np.nan, 95, 88]
}

df = pd.DataFrame(Data)

# Display all missing values using isnull().
print(df.isnull())

# Count the missing values in each column using isnull().sum().
print(df.isnull().sum())

# Create a new DataFrame after removing missing values with dropna().
df=df.dropna()
print(df)

# Fill the missing values with 0 using fillna(0).
print(df.fillna(0))

# Fill the missing values in the Age column with the average age.
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)