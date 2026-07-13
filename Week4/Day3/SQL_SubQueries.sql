-- | StudentID | Name   | Department | Marks |
-- | --------- | ------ | ---------- | ----: |
-- | 1         | Ali    | CS         |    85 |
-- | 2         | Sara   | DS         |    92 |
-- | 3         | Ahmed  | CS         |    78 |
-- | 4         | Umar   | AI         |    92 |
-- | 5         | Ayesha | DS         |    68 |
-- | 6         | Fatima | AI         |    85 |

SELECT Name, Marks
FROM Students
WHERE Marks >
(
SELECT AVG(Marks)
FROM Students
);