-- Employee Database

-- Table: Employees

-- EmployeeID	Name	Department	Salary

-- Write SQL queries to:

-- Classify employees as:
-- High Salary (≥ 100000)
-- Medium Salary (50000–99999)
-- Low Salary (< 50000)
-- Find employees earning more than the average salary.
-- Rank employees by salary using:
-- ROW_NUMBER()
-- RANK()
-- DENSE_RANK()

-- Compare the outputs and explain the difference.

SELECT 
    Name,
    Salary,
    CASE 
        WHEN Salary >= 100000 THEN 'High Salary'
        WHEN Salary >= 50000  THEN 'Medium Salary'
        ELSE 'Low Salary'
    END AS Salary_Class
FROM Employees;

SELECT Name, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);

SELECT 
    Name, 
    Salary,
    ROW_NUMBER() OVER (ORDER BY Salary DESC) AS Row_Num,
    RANK()       OVER (ORDER BY Salary DESC) AS Rank_Num,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS Dense_Rank_Num
FROM Employees;