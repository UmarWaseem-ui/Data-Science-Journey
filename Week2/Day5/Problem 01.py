# Student Dataset
# Create a DataFrame with:

# Name	    Age	    Marks
# Ali	    20	    85
# Ahmed	    22	    78
# Umar	    19	    90
# Sara	    24	    95
# Ayesha	21	    88

# Perform the following:
    # Print only the Name column.
    # Print Name and Marks.
    # Display students whose marks are greater than 85.
    # Display students whose age is less than 22.

import pandas as pd

Students={
    "Name" : ["Ali", "Ahmed", "Umar", "Sara", "Ayesha"],
    "Age" : [20, 22, 19, 24, 21],
    "Marks" : [85, 78, 90, 95, 88]
}

df=pd.DataFrame(Students)

# Print only the Name Column
print(df["Name"])

# Print Name and Marks
print(df[["Name" , "Marks"]])


# Display students whose marks are greater than 85.
print(df[df["Marks"] > 85])

# Display students whose age is less than 22.
print(df[df["Age"] < 22])