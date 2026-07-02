# plt.title() Adds a Title to the Graph
import matplotlib.pyplot as plt

Months = ["Jan","Feb","Mar","Apr"]
Sales = [120,150,170,200]

plt.plot(Months, Sales, label="Sales")
plt.title("Monthly Sales")

# plt.xlable() Adds Label to X-Axis
plt.xlabel("Months")

# plt.ylabel()  Adds Label to Y-Axis
plt.ylabel("Sales")

# plt.grid() Adds Grid lines to the Graph
plt.grid()

# plt.legend() A legend identifies what each line or color represents.
# First Assign a Label 
# plt.plot(Months, Sales, label="Sales")
plt.legend()
plt.show()
