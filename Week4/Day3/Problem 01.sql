-- | StudentID | Name   | Department | Marks |
-- | --------- | ------ | ---------- | ----: |
-- | 1         | Ali    | CS         |    85 |
-- | 2         | Sara   | DS         |    92 |
-- | 3         | Ahmed  | CS         |    78 |
-- | 4         | Umar   | AI         |    92 |
-- | 5         | Ayesha | DS         |    68 |
-- | 6         | Fatima | AI         |    85 |

-- Student Performance

-- Using the Students table:

-- Display each student's name and classify them as:
-- Excellent if Marks ≥ 80
-- Pass if Marks ≥ 60
-- Fail otherwise
-- Find all students who scored above the average marks.
-- Find the student(s) with the highest marks.
-- Create a CTE named PassedStudents that contains only students with marks ≥ 60, then display all rows from it.

SELECT 
    Name,
    CASE 
        WHEN Marks >= 80 THEN 'Excellent'
        WHEN Marks >= 60 THEN 'Pass'
        ELSE 'Fail'
    END AS Classification
FROM Students;

SELECT Name, Marks
FROM Students
WHERE Marks > (SELECT AVG(Marks) FROM Students);

SELECT Name, Marks
FROM Students
WHERE Marks = (SELECT MAX(Marks) FROM Students);

WITH PassedStudents AS (
    SELECT StudentID, Name, Department, Marks
    FROM Students
    WHERE Marks >= 60
)
SELECT * 
FROM PassedStudents;