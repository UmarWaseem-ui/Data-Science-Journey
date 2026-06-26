# Employee Data

# Employees = np.array([
#     [101,25000],
#     [102,30000],
#     [103,35000]
# ])

# Find:
    # Employee IDs column
    # Salaries column
    # Salary of employee 102
    # Shape of array

import numpy as np
Employees = np.array([
     [101,25000],
     [102,30000],
     [103,35000]
 ])

# Shape of Array
print(f"The Shape of Array is: {Employees.shape}")

# Salary of Employee 102
print(f"The Salary of Employee 102 is: {Employees[1,1]}")

# Employees IDs Column
print(f"The Employees IDs are: {Employees[::,0]}")

# Salaries Column
print(f"The Salaries of the Employees are: {Employees[::,1]}")