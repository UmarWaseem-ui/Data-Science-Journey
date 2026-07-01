# School Library Analysis
import matplotlib.pyplot as plt

Books = ["Science", "Math", "English", "History"]
Count = [120, 90, 150, 60]

plt.bar(Books, Count)
plt.show()

plt.pie(Count, labels=Books, autopct="%1.1f%%")
plt.show()

# Here Bar Chart is better to show the Distribution and Book Count