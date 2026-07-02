# Monthly Temperature (Using Seaborn Theme)
# Create:

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# temperature = [18, 20, 25, 30, 35, 38]

# Tasks:
    # Import Seaborn and apply sns.set_theme().
    # Create a line graph.
    # Add a suitable title and axis labels.
    # Add a legend and a grid.
    # Compare the graph with one created without sns.set_theme(). Write down at least two visual differences you notice.

import matplotlib.pyplot as plt
import seaborn as sns

Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Temperature = [18, 20, 25, 30, 35, 38]

# Import Seaborn and apply sns.set_theme().
sns.set_theme()

# Create a line graph.
sns.lineplot(x=Months, y=Temperature, label="Temperature")

# Add a suitable title and axis labels.
plt.title("Monthly Temperature Analysis")
plt.xlabel("Months")
plt.ylabel("Temperature")

# Add a legend and a grid.
plt.grid()
plt.legend()

plt.show()

# Compare the graph with one created without sns.set_theme(). Write down at least two visual differences you notice.
# Background & Grid: sns.set_theme() changes the plain white background to a light gray color with distinct white gridlines.

# Styling & Colors: It replaces Matplotlib's sharp fonts and highly saturated line colors with modern typography and a softer, muted color palette.

