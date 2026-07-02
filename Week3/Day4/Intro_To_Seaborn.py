# Creating a Graph with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

sns.lineplot(x=x, y=y)
plt.show()

# Setting Themes
sns.set_theme()
plt.plot(x,y)
plt.show()