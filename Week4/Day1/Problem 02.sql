CREATE TABLE Employees(
    EMPLOYEEID INT PRIMARY KEY,
    NAMES VARCHAR(20),
    DEPARTMENT VARCHAR(20),
    SALARY INT
)

INSERT INTO Employees(EMPLOYEEID, [NAMES], DEPARTMENT, SALARY)
VALUES
    (101, 'John Doe', 'HR', 55000.00),
    (102, 'Jane Smith', 'IT', 72000.50),
    (103, 'Michael Chang', 'Finance', 68000.00),
    (104, 'Sarah Connor', 'Operations', 59000.00),
    (105, 'David Kim', 'IT', 81000.00),
    (106, 'Emily Watson', 'Marketing', 62500.25)

-- Find the total number of employees.
SELECT COUNT(*)  AS [Total Employees]
FROM Employees

-- Calculate the average salary.
SELECT AVG(SALARY) AS [Average Salary] 
FROM Employees

-- Find the highest salary.
SELECT MAX(SALARY) FROM Employees

-- Calculate the total salary paid by each department.
SELECT DEPARTMENT, SUM(SALARY) FROM Employees
GROUP BY DEPARTMENT

-- Show only departments whose average salary is greater than 50,000.
SELECT DEPARTMENT, AVG(SALARY) FROM Employees
GROUP BY DEPARTMENT
HAVING AVG(SALARY) > 50000
