# Employee Salaries
# 25000, 30000, 35000, 40000, 45000
# Find:
    # Total salary expense
    # Average salary
    # Highest salary
    # Lowest salary

import numpy as np
Array=np.array([25000, 30000, 35000, 40000, 45000])

# Total salary expense
print(f"The Total Salary Expense is: {np.sum(Array)} Rs")

# Average salary
print(f"The Average Salary of an Employee is: {np.mean(Array)} Rs")

# Highest salary
print(f"The Highest Salary of an Employee is: {np.max(Array)} Rs")

# Lowest salary
print(f"The Lowest Salary of an Employee is: {np.min(Array)} Rs")