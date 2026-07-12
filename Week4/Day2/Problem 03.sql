CREATE TABLE MANAGER(
    EMPLOYEEID INT IDENTITY(1, 1),
    NAMES VARCHAR(20),
    MANAGERID INT
)

INSERT INTO MANAGER(NAMES, MANAGERID)
VALUES
('Ali', NULL),
('Sara', 1),
('Ahmad', 1),
('Umar', 2),
('Ayesha', 2)

-- Self Join 
SELECT 
    Emp.NAMES AS Employee, 
    Mgr.NAMES AS Manager
FROM MANAGER Emp
LEFT JOIN MANAGER Mgr 
    ON Emp.MANAGERID = Mgr.EMPLOYEEID;