create DATABASE P1

CREATE TABLE STUDENTS_PERFORMANCE(
    NAMES VARCHAR(20),
    DEPARTMENT VARCHAR(20),
    MARKS INT
)
INSERT INTO STUDENTS_PERFORMANCE(NAMES, DEPARTMENT, MARKS)
VALUES 
('Ali', 'CS', 85),
('Sara', 'CS', 90),
('Ahmed', 'DS', 78),
('Umar', 'DS', 82),
('Ayesha', 'AI', 95)

-- Show all students.
SELECT NAMES FROM STUDENTS_PERFORMANCE

-- Display only students with marks greater than 80.

SELECT * FROM STUDENTS_PERFORMANCE
WHERE MARKS > 80

-- Count the total number of students.
SELECT COUNT(*) FROM STUDENTS_PERFORMANCE

-- Find the average marks of all students.
SELECT AVG(MARKS) FROM STUDENTS_PERFORMANCE

-- Find the highest and lowest marks.
SELECT MAX(MARKS) FROM STUDENTS_PERFORMANCE
SELECT MIN(MARKS) FROM STUDENTS_PERFORMANCE
