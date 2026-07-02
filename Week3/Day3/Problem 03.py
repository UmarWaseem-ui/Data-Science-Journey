# Company Employee Analysis
# A company records employee ages:
    # ages = [22, 24, 25, 26, 28, 29, 30, 32, 35, 38,
    #         40, 42, 45, 47, 50, 52, 55, 58, 60, 62]

# And years of experience:
    # experience = [1, 2, 2, 3, 4, 5, 6, 8, 10, 12,
    #               14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

# Tasks:
    # Plot a histogram of employee ages using bins=6.
    # Plot a scatter plot of Age vs Experience.
    # Determine whether there appears to be a positive, negative, or no correlation, and justify your answer.

import matplotlib.pyplot as plt

Ages = [22, 24, 25, 26, 28, 29, 30, 32, 35, 38,
       40, 42, 45, 47, 50, 52, 55, 58, 60, 62]

Experience = [1, 2, 2, 3, 4, 5, 6, 8, 10, 12,
             14, 16, 18, 20, 22, 24, 26, 28, 30, 32]

plt.hist(Ages, bins=6)
plt.show()

plt.scatter(Ages, Experience)
plt.show()

# It's a Positive Correlation