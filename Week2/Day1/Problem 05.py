# Student Marks Analysis
# 78, 85, 92, 67, 88, 95, 73
# Find:
    # Average marks
    # Highest marks
    # Lowest marks
    # Add 5 bonus marks to every student using array operations

import numpy as np
Array=np.array([78, 85, 92, 67, 88, 95, 73])

# Average marks
print(f"The Average marks of Stuents are: {np.mean(Array):.2f}")
      
# Highest marks
print(f"The Highest marks of a Stuent is: {np.max(Array)}")

# Lowest marks
print(f"The Lowest marks of a Stuents is: {np.min(Array)}")

# Bonus Marks
print("5 Bonus Marks are given to each Student" ,(Array + 5))