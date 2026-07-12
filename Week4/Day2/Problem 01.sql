CREATE DATABASE P2

CREATE TABLE Departments(
    DEPARTMENTID INT PRIMARY KEY,
    DEPARTMENTNAME VARCHAR (30)
)

CREATE TABLE Students(
    STUDENTID INT IDENTITY(1,1) PRIMARY KEY,
    NAMES VARCHAR(20),
    DEPARTMENTID INT    
)

INSERT INTO Departments(DEPARTMENTID, DEPARTMENTNAME)
VALUES
(101, 'Computer Science'),
(102, 'Data Science'),
(103, 'Artificial Intelligence')

INSERT INTO Students(NAMES, DEPARTMENTID)
VALUES
('Ali', 101),
('Sara', 102),
('Ahmad', 101),
('Umar', 105)

-- Display student names with their department names using an INNER JOIN.
SELECT NAMES, DEPARTMENTNAME
FROM Students
INNER JOIN Departments
ON Students.DEPARTMENTID = Departments.DEPARTMENTID

-- Display all students, even if they don't belong to a department (LEFT JOIN).
SELECT NAMES, DEPARTMENTNAME
FROM Students
LEFT JOIN Departments
ON Students.DEPARTMENTID = Departments.DEPARTMENTID

-- Display all departments, even if they have no students (RIGHT JOIN).
SELECT NAMES, DEPARTMENTNAME
FROM Students
RIGHT JOIN Departments
ON Students.DEPARTMENTID = Departments.DEPARTMENTID
