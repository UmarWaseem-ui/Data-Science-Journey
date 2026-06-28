# Reading the CSV _Files and Exploring DataSets
import pandas as pd
# Read dataset.
df = pd.read_csv(...)

# Look at first rows.
df.head()

# Check last rows.
df.tail()

# Check size.
df.shape

# Check columns.
df.columns

# Check data types.
df.info()

# Get statistical summary.
df.describe()