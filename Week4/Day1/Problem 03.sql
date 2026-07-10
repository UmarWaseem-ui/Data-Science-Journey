CREATE TABLE Orders(
    ORDERID INT PRIMARY KEY,
    PRODUCT VARCHAR(20),
    CATEGORY VARCHAR(20),
    QUANTITY INT,
    PRICE DECIMAL(10, 2)
)

INSERT INTO  Orders(ORDERID, PRODUCT, CATEGORY, QUANTITY, PRICE)
VALUES
    (1, 'Laptop', 'Electronics', 1, 1200.00),
    (2, 'Wireless Mouse', 'Electronics', 2, 25.50),
    (3, 'Desk Chair', 'Furniture', 1, 150.00),
    (4, 'Coffee Mug', 'Kitchen', 4, 12.99),
    (5, 'Running Shoes', 'Apparel', 1, 85.00),
    (6, 'Keyboard', 'Electronics', 1, 45.00),
    (7, 'Water Bottle', 'Kitchen', 2, 18.00),
    (8, 'Notebook', 'Stationery', 5, 4.50),
    (9, 'Desk Lamp', 'Furniture', 1, 35.00),
    (10, 'Backpack', 'Apparel', 1, 60.00);

-- Count the total number of orders.
SELECT COUNT(*) AS [Total Orders]
FROM Orders

-- Find the total quantity sold.
SELECT SUM(QUANTITY) AS [QUANTITY SOLD]
FROM Orders

-- Find the average price of products.
SELECT AVG(PRICE) AS [AVERAGE PRICE]
 FROM Orders

-- Calculate the total sales for each category (SUM(Quantity * Price)).
SELECT CATEGORY, SUM(QUANTITY * PRICE) AS [Total Sales]
FROM Orders
GROUP BY CATEGORY

-- Display only categories whose total sales exceed 10,00.
SELECT CATEGORY, SUM(QUANTITY * PRICE) AS [Total Sales]
FROM Orders
GROUP BY CATEGORY
HAVING SUM(QUANTITY * PRICE) > 1000

-- Sort the categories by total sales in descending order.
SELECT CATEGORY, SUM(QUANTITY * PRICE) AS [Total Sales]
FROM Orders
GROUP BY CATEGORY 
ORDER BY [Total Sales] DESC;