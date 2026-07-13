-- Online Store

-- Table: Products

-- ProductID	ProductName	Category	Sales

-- Write SQL queries to:

-- Find products whose sales are above the average sales.
-- Create a CTE called TopProducts for products with sales greater than 1000.
-- Rank all products by sales using DENSE_RANK().
-- Label products using CASE WHEN:
-- Best Seller if Sales ≥ 2000
-- Popular if Sales ≥ 1000
-- Regular otherwise

SELECT ProductName, Sales
FROM Products
WHERE Sales > (SELECT AVG(Sales) FROM Products);

WITH TopProducts AS (
    SELECT ProductID, ProductName, Category, Sales
    FROM Products
    WHERE Sales > 1000
)
SELECT * 
FROM TopProducts;

SELECT 
    ProductName, 
    Sales,
    DENSE_RANK() OVER (ORDER BY Sales DESC) AS Sales_Rank
FROM Products;

SELECT 
    ProductName,
    Sales,
    CASE 
        WHEN Sales >= 2000 THEN 'Best Seller'
        WHEN Sales >= 1000 THEN 'Popular'
        ELSE 'Regular'
    END AS Product_Label
FROM Products;