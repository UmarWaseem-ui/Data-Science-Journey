import numpy as np

Students = np.array([
    [80,90,70],
    [85,95,75], # This is a 2D Array
    [88,92,78]
])

#       C0  C1  C2

# R0    80  90  70
# R1    85  95  75
# R2    88  92  78

# Dimensions
print(Students.ndim) # Tells you the Dimension (Rows + Columns)

# Shape
print(Students.shape) # Tells you no. of Rows And Columns

# Accessing 2D 1st Elements
print(Students[0,0]) # [Row, Column]

# Accessing 2nd Row and 3rd Column
print(Students[1, 2]) 

# Accessing last Element
print(Students[-1,-1])

#  Accessing Entire Row
print(Students[0])

#  Accessing Entire Column
print(Students[:,0])