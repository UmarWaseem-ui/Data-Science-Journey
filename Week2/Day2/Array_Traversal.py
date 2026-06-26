# Traversal means visiting every element.
import numpy as np
Array = np.array([1,2,3,4,5,6])

for x in Array: # Print Every Element from Start to Finish
    print(x)

# 2D Traversal
Array1 = np.array([
    [1,2],
    [3,4]
])

for row in Array1: # print the Rows
    print(row) 

for row in Array1:
    for element in row:
        print(element) # Print elements in the Rows