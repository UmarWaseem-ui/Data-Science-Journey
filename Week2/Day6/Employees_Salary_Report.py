# Dataset
# Name	    Department	    Salary	    Bonus	Experience
# Ali	    IT	            50000	    5000	    2
# Ahmed	    HR	            60000	    7000	    5
# Sara	    Finance	        55000	    6000	    3
# Umar	    IT	            70000	    8000	    7

# Find
    # Average Salary
    # Average Bonus
    # Highest Salary
    # Lowest Salary
    # Highest Bonus
    # Lowest Bonus

# Add New Column
# Create:
    # Total Income = Salary + Bonus
    # Tax = 10% of Salary
    # Net Income = Total Income - Tax
    # Performance Grade

# Filter
# Display employees:
    # Whose Salary is greater than 55000
    # Whose Experience is greater than 3 years
    # Whose Department is IT

# Bonus Challenge 
    # df.sort_values()
    # df.groupby()
    # df.value_counts()

# Then solve:
    # Show employees sorted by Salary (highest first).
    # Find the average salary of each department.
    # Count how many employees are in each department.

import pandas as pd

Data={
    "Name" : ["Ali", "Ahmed", "Sara", "Umar"],
    "Department" : ["IT", "HR", "Finance", "IT"],
    "Salary" : [50000, 60000, 55000, 70000],
    "Bonus" : [5000, 7000, 6000, 8000],
    "Experience" : [2, 5, 3, 7]
}

df=pd.DataFrame(Data)

# Average Salary
print(f"The Average Salary of Employees is: {df["Salary"].mean()}")

# Average Bonus
print(f"\nThe Average Bonus of Employees is: {df["Bonus"].mean()}")

# Highest Salary
print(f"\nThe Highest Salary of any Employee is: {df["Salary"].max()}")

# Lowest Salary
print(f"\nThe Lowest Salary of any Employee is: {df["Salary"].min()}")

# Highest Bonus
print(f"\nThe Highest Bonus of any Employee is: {df['Bonus'].max()}")

# Lowest Bonus
print(f"\nThe Lowest Bonus of any Employee is: {df['Bonus'].min()}")

# Creating Column Total Income
df["Total Income"]= df[["Bonus", "Salary"]].sum(axis=1)

# Creating Column Tax
df["Tax"]= df["Salary"] / 10

# Creating Column Net Income
df["Net Income"]= df["Total Income"].sub(df["Tax"])

# Creating Performance Column
def Grade(row):
    if row["Salary"] > 60000 and row["Experience"] > 5:
        return "A+"
    elif row["Salary"] > 55000 and row["Experience"] > 4:
        return "A"
    elif row["Salary"] > 50000 and row["Experience"] >= 3:
        return "B"
    else:
        return "C"
    
df["Grade"]= df.apply(Grade, axis=1)

# Employee Salary Greater than 55000
df[df["Salary"] > 55000]

# Employee Experience Greater than 3 years
df[df["Experience"] > 3]

# IT Department Employee
df[df["Department"] == "IT"]

# Sort by Salary in Ascending Order
sorted_df = df.sort_values(by="Salary", ascending=False)
print(sorted_df)

# Calculate Average Salary per Department
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

# Count Employees per Department
dept_counts = df["Department"].value_counts()
print(dept_counts)