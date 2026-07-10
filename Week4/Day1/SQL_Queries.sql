create DATABASE VSCODE

-- 1. Create the Students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL,
    Age INT,
    Department NVARCHAR(10),
    Marks INT
);

-- 2. Insert your data into the table
INSERT INTO Students (StudentID, Name, Age, Department, Marks)
VALUES 
    (1, 'Ali', 20, 'CS', 85),
    (2, 'Ahmed', 22, 'DS', 90),
    (3, 'Sara', 21, 'CS', 88),
    (4, 'Ayesha', 20, 'AI', 95),
    (5, 'Umar', 23, 'DS', 76);

-- 3. Verify the data was inserted successfully
SELECT * FROM Students;

-- Filter rows
SELECT * FROM Students
WHERE Marks > 80;

-- Sort data
SELECT * FROM Students
ORDER BY Marks DESC;

-- Show first 5 rows
SELECT TOP(5)* FROM Students


-- Unique values
SELECT DISTINCT Department
FROM Students;

-- Aggregate Functions
SELECT COUNT(*) FROM Students;
SELECT SUM(Marks) FROM Students;
SELECT AVG(Marks) FROM Students;
SELECT MIN(Marks) FROM Students;
SELECT MAX(Marks) FROM Students;

-- Grouping
SELECT Department, AVG(Marks)
FROM Students
GROUP BY Department;

-- Filter grouped data
SELECT Department, AVG(Marks)
FROM Students
GROUP BY Department
HAVING AVG(Marks) > 80;