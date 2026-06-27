# A Series is a one-dimensional labeled arra (A single column of Data)
# Creating a Series
import pandas as pd
Marks=pd.Series([10, 20, 30])
print(Marks)

# Creating a Series with your own Index
Marks1=pd.Series([10, 20, 30, 40, 50],
                index=["Ali","Ahmad","Umar","Usman","Ahsan"])
print(Marks1)

# Accessing Values from the Series
# By Index Position
print(Marks1.iloc[0])

# # By Label(Value)
print(Marks1["Ahmad"])