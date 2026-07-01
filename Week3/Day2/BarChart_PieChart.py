# Creating a Bar Chart
import matplotlib.pyplot as plt

Students = ["Ali", "Ahmed", "Umar", "Sara"]
Marks = [85, 90, 78, 95]

plt.bar(Students, Marks)
#plt.show()

# Creating a Pie Chart
Departments = ["CS", "AI", "DS", "SE"]
students = [40,30,20,10]

plt.pie(students, labels=Departments, autopct="%1.1f%%") # autopct=%1.1f%% tells you the percentage of distribution
plt.show()