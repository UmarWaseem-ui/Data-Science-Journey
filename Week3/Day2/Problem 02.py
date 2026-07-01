# Monthly Expenses
import matplotlib.pyplot as plt

Categories = ["Food", "Rent", "Transport", "Internet", "Entertainment"]
Expenses = [350, 800, 200, 100, 150]

plt.pie(Expenses, labels=Categories, autopct="%1.1f%%")
plt.show()