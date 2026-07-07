# Employee Dataset
# Create a DataFrame with the following columns:
    # Age
    # Experience
    # Salary
    # Working_Hours
# Add at least 8 employees.

# Tasks:
    # Compute the correlation matrix.
    # Create a heatmap with annotations.
    # Identify which feature has the strongest correlation with Salary.
    # Explain why that feature might influence salary.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = {
    'Age': [25, 32, 45, 29, 38, 41, 23, 35],
    'Experience': [2, 8, 20, 5, 12, 15, 1, 10],
    'Salary': [50000, 75000, 120000, 62000, 95000, 110000, 45000, 85000],
    'Working_Hours': [40, 40, 45, 35, 40, 50, 40, 45]
}

df=pd.DataFrame(Data)

# Compute the correlation matrix.
corr=df.corr()

# Create a heatmap with annotations.
sns.heatmap(corr, annot=True)

plt.show()

# Identify which feature has the strongest correlation with Salary.
# Experience

# Explain why that feature might influence salary.
# Experience is the most direct measure of professional value.