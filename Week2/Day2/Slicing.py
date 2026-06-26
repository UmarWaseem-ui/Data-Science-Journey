# Slicing means extracting multiple values.
import numpy as np
Array=np.array([10, 20, 30, 40, 50])

print(Array[1:4])

# Accessing Value from the Beginning
print(Array[:3]) # This means the first value is from 0 Index

# Accessing Value from the End
print(Array[2:]) # This means every value till end rom Index 2

# Accessing Every Second Element
print(Array[::2])

# Or same can be written as
print(Array[0:5:2])