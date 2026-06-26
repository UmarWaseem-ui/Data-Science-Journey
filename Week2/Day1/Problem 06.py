# Store Inventory
# 50, 30, 20, 45, 60
# A new shipment arrives adding 10 items to every product.

# Using NumPy operations:
    # Update inventory
    # Find total inventory
    # Find product with highest stock
    # Find product with lowest stock

import numpy as np
Array=np.array([50, 30, 20, 45, 60])

# Update inventory
print("Adding 10 items to each Product:", Array + 10)

# Total Inventory
print(f"The Total Inventory is: {np.sum(Array)}")

# Highest Stock
print(f"The Highest Stock is: {np.max(Array)}")

# Lowest Stock
print(f"The Lowest Stock is: {np.min(Array)}")