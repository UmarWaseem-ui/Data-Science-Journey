import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.DataFrame()

# Create correlation matrix
corr = df.corr()

# Create heatmap
sns.heatmap(corr)

plt.show()

# Heatmap with values
sns.heatmap(corr, annot=True)

plt.show()