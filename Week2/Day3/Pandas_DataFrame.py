# A DataFrame is a collection of multiple Series (A complete Table)
# Creating a DataFrame
import pandas as pd
Data={
    "Name": ["Ali", "Ahmad", "Umar"],
    "Age" : [20, 21, 19],
    "Marks": [88, 90, 92]
}

DF=pd.DataFrame(Data)
print(DF)

# Accessing Columns
print(DF["Name"])