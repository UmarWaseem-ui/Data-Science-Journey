# Mini Project
# Student Performance Dashboard

# Dataset:
# Use either:

# Student Performance Dataset
# Titanic Dataset
# Iris Dataset

# Perform
    # Data Analysis
    # Read CSV
    # Explore dataset
    # Check missing values

# Create Graphs
# At minimum:
    # Line Chart
    # Bar Chart
    # Histogram
    # Pie Chart
    # Scatter Plot
    # Heatmap

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("Student_Data.csv")
print(df.head(3))
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Line Chart
sns.set_theme()
plt.figure(figsize=(10,5))

plt.plot(df.index, df["G3"], label="Final Grade (G3)")

plt.title("Final Grades of Students")

plt.xlabel("Student Number")

plt.ylabel("Final Grade")

plt.grid(True)

plt.legend()

# Bar Chart
Avg_Grades = [
    df["G1"].mean(),
    df["G2"].mean(),
    df["G3"].mean()
]

Exams = ["G1","G2","G3"]

plt.figure(figsize=(6,5))

plt.bar(Exams, Avg_Grades)

plt.title("Average Grades in G1, G2 and G3")

plt.xlabel("Exam")

plt.ylabel("Average Marks")

plt.grid(axis="y")

# Histogram
plt.figure(figsize=(8,5))

plt.hist(df["G3"], bins=10)

plt.title("Distribution of Final Grades")

plt.xlabel("Final Grade")

plt.ylabel("Number of Students")

plt.grid(True)

# Pie Chart
Passed = (df["G3"] >= 10).sum()
Failed = (df["G3"] < 10).sum()

plt.figure(figsize=(6,6))

plt.pie(
    [Passed, Failed],
    labels=["Passed","Failed"],
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail")

# Scatter Plot
plt.figure(figsize=(8,5))

plt.scatter(df["studytime"], df["G3"])

plt.title("Study Time vs Final Grade")

plt.xlabel("Study Time")

plt.ylabel("Final Grade")

plt.grid(True)

# Heatmap
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10,8))

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Matrix")

plt.show()