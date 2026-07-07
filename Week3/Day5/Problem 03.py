# House Price Analysis
# Create the following DataFrame:
# data = {
#     "Area": [800, 1000, 1200, 1500, 1800, 2000],
#     "Bedrooms": [2, 2, 3, 3, 4, 4],
#     "Bathrooms": [1, 2, 2, 2, 3, 3],
#     "Price": [150000, 180000, 220000, 280000, 340000, 380000]
# }

# Tasks:
    # Create the DataFrame.
    # Generate the correlation matrix.
    # Plot a heatmap with annot=True.
    # Determine which feature is most strongly correlated with Price.
    # Write a short explanation (3–4 sentences) on how a Data Scientist could use this information before building a house price prediction model.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = {
    "Area": [800, 1000, 1200, 1500, 1800, 2000],
    "Bedrooms": [2, 2, 3, 3, 4, 4],
    "Bathrooms": [1, 2, 2, 2, 3, 3],
    "Price": [150000, 180000, 220000, 280000, 340000, 380000]
}

# Create the DataFrame.
df=pd.DataFrame(Data)

# Generate the correlation matrix.
corr=df.corr()

# Plot a heatmap with annot=True.
sns.heatmap(corr, annot=True)

plt.show()

# Determine which feature is most strongly correlated with Price.
# Area

# Write a short explanation (3–4 sentences) on how a Data Scientist could use this information before building a house price prediction model.
# Analyzing the correlation matrix allows a Data Scientist to perform feature selection, identifying Area as the strongest baseline predictor for house prices.
# It highlights risks of multicollinearity among the features, signaling the need to drop redundant variables or apply regularization techniques like Ridge or Lasso regression.