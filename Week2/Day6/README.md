# Day 6 - Mini Projects: Data Analysis with Pandas

## Objective

To apply the concepts learned throughout Week 2 by performing data analysis on real-world datasets using NumPy and Pandas. The goal is to analyze, manipulate, filter, and save data while gaining hands-on experience with common Data Science tasks.

---

## Mini Project 1 - Student Performance Analysis

### Dataset

| Name  | Math | Physics | English |
| ----- | ---- | ------- | ------- |
| Ali   | 80   | 75      | 90      |
| Ahmed | 85   | 95      | 88      |
| Umar  | 78   | 82      | 86      |

### Tasks Performed

* Calculated the average marks of each student
* Found the highest marks
* Found the lowest marks
* Added new columns:

  * Total Marks
  * Average Marks
  * Grade
* Filtered students with an average score greater than 80
* Saved the updated dataset to a new CSV file using `to_csv()`

---

## Mini Project 2 - Employee Salary Report

### Dataset

| Name  | Department | Salary | Bonus | Experience |
| ----- | ---------- | ------ | ----- | ---------- |
| Ali   | IT         | 50000  | 5000  | 2          |
| Ahmed | HR         | 60000  | 7000  | 5          |
| Sara  | Finance    | 55000  | 6000  | 3          |
| Umar  | IT         | 70000  | 8000  | 7          |

### Tasks Performed

* Calculated:

  * Average Salary
  * Average Bonus
  * Highest Salary
  * Lowest Salary
  * Highest Bonus
  * Lowest Bonus
* Added new columns:

  * Total Income
  * Tax (10% of Salary)
  * Net Income
  * Performance Grade
* Applied filters to display:

  * Employees with Salary greater than 55,000
  * Employees with more than 3 years of experience
  * Employees working in the IT department
* Performed advanced operations:

  * Sorted employees by salary
  * Calculated the average salary for each department
  * Counted employees in each department

---

## Functions Learned

* `to_csv()`
* `sort_values()`
* `groupby()`
* `value_counts()`

---

## Files

* student_performance_analysis.py
* employee_salary_report.py
* student_performance.csv
* employee_salary_report.csv
* updated_student_performance.csv

---

## Key Learnings

* Applied NumPy and Pandas concepts to solve real-world data analysis problems.
* Created new columns using existing data.
* Filtered datasets using conditional statements.
* Organized and summarized data using grouping and sorting.
* Exported processed datasets into CSV files.
* Understood the complete workflow of basic data analysis using Pandas.

---

## Outcome

After completing Day 6, I can:

* Analyze structured datasets using Pandas
* Perform statistical calculations on data
* Create new features from existing columns
* Filter and organize datasets efficiently
* Save processed data to CSV files
* Apply the complete data analysis workflow to beginner-level projects
