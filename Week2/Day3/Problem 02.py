# Employee Data
# Create a DataFrame with the following information:

# Name	Department	Salary
# Ali	IT	        50000
# Ahmed	HR	        45000
# Umar	Finance	    55000

# Then:
    # Print the DataFrame.
    # Print only the Salary column.
    # Print only the Department column.

import pandas as pd
Data={
    "Name" : ["Ali", "Ahmad", "Umar"],
    "Department" : ["IT" ,"HR", "Finance"],
    "Salary" : [50000, 45000, 55000]
}

# Print The DataFrame
EmployeeData=pd.DataFrame(Data)
print(EmployeeData)

# Print only the Salary column.
print(EmployeeData["Salary"])

# Print only the Department column.
print(EmployeeData["Department"])