# Student Marks Analysis
# Create the following data:

# students = ["Ali", "Ahmed", "Umar", "Sara", "Ayesha"]
# marks = [78, 92, 85, 95, 88]

# Tasks:
    # Plot a line graph.
    # Add the title "Student Marks Analysis".
    # Label the x-axis as "Students".
    # Label the y-axis as "Marks".
    # Add a grid.
    # Add a legend with the label "Marks".

import matplotlib.pyplot as plt

Students = ["Ali", "Ahmed", "Umar", "Sara", "Ayesha"]
Marks = [78, 92, 85, 95, 88]

# Plot a Line Graph
plt.plot(Students, Marks, label="Marks")

# Add the title "Student Marks Analysis".
plt.title("Students Marks Analysis")

# Label the x-axis as "Students".
plt.xlabel("Students")

# Label the y-axis as "Marks".
plt.ylabel("Marks")

# Add a grid.
plt.grid()

# Add a legend with the label "Marks".
plt.legend()

plt.show()