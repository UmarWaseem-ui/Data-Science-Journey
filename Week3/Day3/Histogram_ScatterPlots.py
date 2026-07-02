# Creating a Histogram
import matplotlib.pyplot as plt

Marks = [55,58,60,62,64,67,70,71,73,75,
         78,80,82,84,86,88,90,92,95,98]

plt.hist(Marks, bins=5)
#plt.show()

# Creating a Scatter Plot
import matplotlib.pyplot as plt

Hours = [2,3,4,5,6,7]
Marks = [50,60,65,72,80,88]

plt.scatter(Hours, Marks)
plt.show()