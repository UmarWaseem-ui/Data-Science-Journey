import numpy as np
Array = np.array([10,20,30,40,50])

# Reverse Array
print(Array[::-1])

# Modifying Values
Array[0]=100 # This updates the Value at 0 Index
print(Array)

# Modifying Multiple Values
Array[1:4]=60
print("New Array is: ", Array)