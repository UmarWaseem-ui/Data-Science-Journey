# Employee Dataset
# Create a DataFrame with:
    # Employee Name
    # Department
    # Salary
# Add at least 6 employees.

# Then:
    # Display employees with salaries greater than 60,000.
    # Display employees from the IT department.
    # Display employees whose salary is between 50,000 and 70,000 using multiple conditions.
    # Display employees whose salary is between 50,000 and 70,000 using multiple conditions.

import pandas as pd

Employee={
    "Name" : ["Ali", "Ahmad", "Usman", "Fahad", "Sana", "Usama"],
    "Department" : ["Finance", "IT", "Sales", "HR", "Accountant", "Management"],
    "Salary" : [60000, 55000, 50000, 45000, 65000, 70000]
}

df=pd.DataFrame(Employee)

# Display employees with salaries greater than 60,000.
print(df[df["Salary"] > 60000])

# Display employees from the IT department.
print(df[df["Department"] == "IT"])

# Display employees whose salary is between 50,000 and 70,000 using multiple conditions.
print(df[(df["Salary"] > 50000) & (df["Salary"] < 70000)])