# Reshape Challenge

# arr = np.arange(1,13)

# Convert it into:
# 3 rows × 4 columns

# Then:
# 4 rows × 3 columns

# Access:
    # First row
    # Last column
    # Middle elements

import numpy as np
Array=np.arange(1,13)

# Converting into 3 x 4 Matric
print(Array.reshape(3, 4))

# Converting into 4 x 3 Matric
Array1=Array.reshape(4, 3)
print(Array1)

# Accessing the First Row
print(Array1[0])

# Accessing the Last Column
print(Array1[:,-1])

# Accessing the Middle Elements
print(Array1[:,1])