-- SYNTAX
-- WITH TableName AS
-- (
--     SELECT ...
-- )

-- SELECT *
-- FROM TableName;

WITH TopStudents AS
(
SELECT *
FROM Students
WHERE Marks > 80
)

SELECT *
FROM TopStudents;