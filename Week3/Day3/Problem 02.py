# Exercise vs Calories Burned
# Create the following data:

# hours_exercise = [1, 2, 3, 4, 5, 6, 7]
# calories_burned = [180, 250, 320, 410, 500, 590, 680]

# Tasks:
    # Create a scatter plot.
    # Decide whether the relationship is positive, negative, or no correlation.
    # Explain your answer in 2–3 sentences.

import matplotlib.pyplot as plt

Hours_exercise = [1, 2, 3, 4, 5, 6, 7]
Calories_burned = [180, 250, 320, 410, 500, 590, 680]

# Create a Scatter Plot
plt.scatter(Hours_exercise, Calories_burned)
plt.show()

# It is a Positive Correlation as the points in Both Axis are increasing Simultaniously