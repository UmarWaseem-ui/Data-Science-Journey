-- | StudentID | Name   | Department | Marks |
-- | --------- | ------ | ---------- | ----: |
-- | 1         | Ali    | CS         |    85 |
-- | 2         | Sara   | DS         |    92 |
-- | 3         | Ahmed  | CS         |    78 |
-- | 4         | Umar   | AI         |    92 |
-- | 5         | Ayesha | DS         |    68 |
-- | 6         | Fatima | AI         |    85 |

-- SYNTAX
-- CASE
--     WHEN condition THEN result
--     WHEN condition THEN result
--     ELSE result
-- END

SELECT
Name,
Marks,

CASE
    WHEN Marks >= 80 THEN 'Excellent'
    WHEN Marks >= 60 THEN 'Pass'
    ELSE 'Fail'
END AS Result

FROM Students;