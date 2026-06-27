# Student Marks
# Create a Series containing the marks:
# 78, 85, 92, 88, 75

# Then:
    # Print the Series.
    # Use student names as the index.
    # Display the marks of Ahmed.

import pandas as pd
Marks=pd.Series([78, 85, 92, 88, 75])

# Print the Series
print(Marks)

# Use student names as the index
Marks1=pd.Series([78, 85, 92, 88, 75],
                index=["Ali", "Ahmad", "Umar", "Usman", "Aliza"])
print(Marks1)

# Display the marks of Ahmed
print(Marks1["Ahmad"])
