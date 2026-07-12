CREATE TABLE Customers(
    CUSTOMERID INT IDENTITY(1,1) PRIMARY KEY,
    NAMES VARCHAR(20)
)

CREATE TABLE Orders(
    ORDERID INT PRIMARY KEY,
    CUSTOMERID INT,
    AMOUNT INT
)

INSERT INTO Customers(NAMES)
VALUES
('Ali'),
('Sara'),
('Ahmad')

INSERT INTO Orders(ORDERID, CUSTOMERID, AMOUNT)
VALUES
(101, 1, 500),
(102, 1, 700),
(103, 2, 400)

-- Show each customer's name and order amount using an INNER JOIN.
SELECT NAMES, AMOUNT
FROM Customers
INNER JOIN Orders
ON Customers.CUSTOMERID= Orders.CUSTOMERID

-- Show all customers, including those with no orders (LEFT JOIN).
SELECT NAMES, AMOUNT
FROM Customers
LEFT JOIN Orders
ON Customers.CUSTOMERID= Orders.CUSTOMERID

-- Identify customers who have never placed an order.
SELECT NAMES
FROM Customers
LEFT JOIN Orders
ON Customers.CUSTOMERID = Orders.CUSTOMERID
WHERE Orders.CUSTOMERID IS NULL;