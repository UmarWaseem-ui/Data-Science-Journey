import pandas as pd

Data = {
    "Name": ["Ali", "Ahmed", "Umar", "Sara", "Ayesha"],
    "Age": [20, 22, 19, 24, 21],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(Data)
print(df)

# Selecting Single Column
print(df["Age"])

# Selecting Multiple Coulmns
print(df[["Age", "Marks"]])

# Filtering Rows
print(df[df["Age"] > 20])

# With Multiple Conditions using AND
print(df[(df["Age"] > 20) & (df["Marks"] > 80)])

# With Multiple Conditions using OR
print(df[(df["Age"] < 20) | (df["Marks"] > 90)])

# Handling Missing Values
print(df.isnull()) # True = Missing Value

# To Count Missing Values
print(df.isnull().sum()) 

# Removing Missing Values
print(df.dropna()) # Does not change the Original DataFrame
df=df.dropna() # Changes the DataFrame

# Filling Missing values
df.fillna(0) # Fill Missing Values with 0

# Filling with Average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())