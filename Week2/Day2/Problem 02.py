# Student Marks Table

# marks = np.array([
#     [78,85,90],
#     [88,92,80],
#     [70,75,85]
# ])

# Find:
    # First student marks
    # Second subject marks
    # Average marks of each student
    # Average marks of each subject

import numpy as np
Marks = np.array([
     [78,85,90],
     [88,92,80],
     [70,75,85]
])

# First Student Marks
print(f"The Marks of First Student are: {Marks[0]}")

# Second Subject Marks
print(f"The Second Subject Marks are: {Marks[::,1]}")

# Average Marks of Each Student
print(f"The Average Marks of Each Student are: {np.mean(Marks, axis=1)}") # Axis= 1 means (Row by Row)

# Average Marks of Each Subject
print(f"The Average Marks of Each Subject are: {np.mean(Marks, axis=0)}") # Axis= 0 means (Column by Column)