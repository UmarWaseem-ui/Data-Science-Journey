# Student Dataset
# Create the following DataFrame:
# data = {
#     "Hours_Studied": [2, 3, 4, 5, 6, 7],
#     "Marks": [45, 55, 68, 78, 88, 95],
#     "Sleep_Hours": [8, 7.5, 7, 6.5, 6, 5.5]
# }

# Tasks:
    # Convert the dictionary into a DataFrame.
    # Calculate the correlation matrix using df.corr().
    # Display the correlation matrix as a heatmap using sns.heatmap().
    # Add annot=True to display the correlation values.
    # Based on the heatmap, identify one positive and one negative correlation.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = {
     "Hours_Studied": [2, 3, 4, 5, 6, 7],
     "Marks": [45, 55, 68, 78, 88, 95],
     "Sleep_Hours": [8, 7.5, 7, 6.5, 6, 5.5]
}

# Convert the dictionary into a DataFrame.
df=pd.DataFrame(Data)

# Calculate the correlation matrix using df.corr().
corr=df.corr()

# Display the correlation matrix as a heatmap using sns.heatmap().
sns.heatmap(corr)

# Add annot=True to display the correlation values.
sns.heatmap(corr, annot=True)

plt.show()

# Based on the heatmap, identify one positive and one negative correlation.
# Hours_Studied and Marks (Positie Correlation)
# Sleep_Hours and Marks (Negative Correlation)