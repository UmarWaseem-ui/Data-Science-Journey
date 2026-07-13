-- ROW_NUMBER()

-- Purpose
-- Assigns a unique number to every row.

SELECT
Name,
Marks,

ROW_NUMBER() OVER
(
ORDER BY Marks DESC
)
AS RowNum

FROM Students;

-- RANK()

-- Purpose:
-- Give ranking.

SELECT
Name,
Marks,

RANK() OVER
(
ORDER BY Marks DESC
)
AS Ranking

FROM Students;

-- DENSE_RANK()

-- Very similar.
-- But no gaps.

SELECT
Name,
Marks,

DENSE_RANK() OVER
(
ORDER BY Marks DESC
)
AS DenseRank

FROM Students;