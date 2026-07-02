# Company Sales Report
# Create:

# products = ["Laptop", "Phone", "Tablet", "Watch"]
# sales = [120, 200, 90, 150]

# Tasks:
    # Draw a bar chart.
    # Add the title "Product Sales Report".
    # Label both axes appropriately.
    # Add a grid.

import matplotlib.pyplot as plt
import seaborn as sns

Products = ["Laptop", "Phone", "Tablet", "Watch"]
Sales = [120, 200, 90, 150]

sns.set_theme()

# Draw a bar chart.
plt.bar(Products, Sales)

# Add the title "Product Sales Report".
plt.title("Product Sales Report")

# Label both axes appropriately.
plt.xlabel("Products")
plt.ylabel("Sales")

# Add a grid.
plt.grid()

plt.show()
