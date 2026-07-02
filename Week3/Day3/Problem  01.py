# Student Marks Distribution
# Create a list of marks for 20 students.

# Tasks:
    # Plot a histogram.
    # Use bins=5.
    # Observe which score range has the highest number of students.

import matplotlib.pyplot as plt
Marks = [55,58,60,62,64,67,70,71,73,75,
         78,80,82,84,86,88,90,92,95,98]

# Plot a Histogram, Bins= 5
plt.hist(Marks, bins=5)
plt.show()

# All bins have Equal number of Students