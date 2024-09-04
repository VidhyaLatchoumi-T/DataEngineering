--1. Calculate the total amount spent by each customer.
SELECT CustomerId, SUM(TotalAmount) AS TotalAmount
FROM Orders
GROUP BY CustomerId;

--2. Find customers who have spent more than $1,000 in total.
SELECT CustomerId, SUM(TotalAmount) AS TotalAmount
FROM Orders
GROUP BY CustomerId
HAVING SUM(TotalAmount) > 1000;

--3. Find Product Categories with More Than 5 Products
SELECT Category, COUNT(ProductID) AS NumberOfProducts
FROM Products
GROUP BY Category
HAVING COUNT(ProductID) > 5;

--4. Calculate the total number of products for each category and supplier combination.
SELECT p.CategoryId, s.SupplierId, COUNT(p.ProductId) AS TotalProducts
FROM Products p
JOIN Supplier s ON p.SupplierId = s.SupplierId
GROUP BY p.CategoryId, s.SupplierId;

--5. Summarize total sales by product and customer, and also provide an overall total.
SELECT p.ProductName,c.CustomerName,SUM(s.SaleAmount) AS TotalSales
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
JOIN Customers c ON s.CustomerID = c.CustomerID
GROUP BY p.ProductName, c.CustomerName
ORDER BY p.ProductName, c.CustomerName;

SELECT SUM(SaleAmount) AS OverallTotalSales
FROM Sales;

--Stored Procedure with Insert Operation
CREATE PROCEDURE InsertOperation
	@ProductID INT,
	@ProductName NVARCHAR(50),
	@Category NVARCHAR(50),
	@Price INT,
	@StockQuantity INT
AS
BEGIN 
	INSERT INTO Products(ProductId,ProductName,Category,Price,StockQuantity)
	VALUES(@ProductId,@ProductName,@Category,@Price,@StockQuantity)
END;
EXEC InsertOperation 6,'Bluetooth','Electronics',8000,8;

--Stored Procedure with Update Operation
CREATE PROCEDURE UpdateOperation
	@ProductID INT,
	@StockQuantity INT
AS
BEGIN 
	UPDATE Products
	SET StockQuantity=@StockQuantity
	WHERE ProductID=@ProductID
END;
EXEC UpdateOperation 6,10

--Stored Procedure with Delete Operation
CREATE PROCEDURE DeleteOperation
	@ProductID INT
AS
BEGIN 
	DELETE FROM Products
	WHERE ProductID=@ProductID
END;
EXEC DeleteOperation 6

--1. Hands-on Exercise: Filtering Data using SQL Queries
--Retrieve all products from the Products table that belong to the category 'Electronics' and have a price greater than 500.
SELECT * FROM Products
WHERE Category = 'Electronics' AND Price > 500;

--2. Hands-on Exercise: Total Aggregations using SQL Queries
--Calculate the total quantity of products sold from the Orders table.
SELECT SUM(Quantity) AS TotalQuantitySold
FROM Orders;

--3. Hands-on Exercise: Group By Aggregations using SQL Queries
--Calculate the total revenue generated for each product in the Orders table.
SELECT ProductID, SUM(Quantity * TotalAmount) AS TotalRevenue
FROM Orders
GROUP BY ProductID;

--4. Hands-on Exercise: Order of Execution of SQL Queries
--Write a query that uses WHERE, GROUP BY, HAVING, and ORDER BY clauses and explain the order of execution.
SELECT ProductID, SUM(Quantity) AS TotalQuantity
FROM Orders
WHERE OrderDate >= '2023-01-01'
GROUP BY ProductID
HAVING SUM(Quantity) > 3
ORDER BY TotalQuantity DESC;

--5. Hands-on Exercise: Rules and Restrictions to Group and Filter Data in SQL Queries
--Write a query that corrects a violation of using non-aggregated columns without grouping them.
SELECT ProductID, SUM(Quantity) AS TotalQuantity
FROM Orders
GROUP BY ProductID;

--6. Hands-on Exercise: Filter Data based on Aggregated Results using Group By and Having
--Retrieve all customers who have placed more than 5 orders using GROUP BY and HAVING clauses.
SELECT CustomerID
FROM Orders
GROUP BY CustomerID
HAVING COUNT(OrderID) > 5;


--1. Basic Stored Procedure
--Create a stored procedure named GetAllCustomers that retrieves all customer details from the Customers table.
CREATE PROCEDURE GetAllCustomers
AS
BEGIN
    SELECT * FROM Customers;
END;
EXEC GetAllCustomers

--2. Stored Procedure with Input Parameter
--Create a stored procedure named GetOrderDetailsByOrderID that accepts an OrderID as a parameter and retrieves the order details for that specific order.
CREATE PROCEDURE GetOrderDetailsByOrderID
    @OrderID INT
AS
BEGIN
    SELECT * FROM Orders WHERE OrderID = @OrderID;
END;
EXEC GetOrderDetailsByOrderID 2

--3. Stored Procedure with Multiple Input Parameters
--Create a stored procedure named GetProductsByCategoryAndPrice that accepts a product Category and a minimum Price as input parameters and retrieves all products that meet the criteria.
CREATE PROCEDURE GetProductsByCategoryAndPrice
    @Category NVARCHAR(50),
    @MinPrice INT
AS
BEGIN
    SELECT * FROM Products
    WHERE Category = @Category AND Price >= @MinPrice;
END;
EXEC GetProductsByCategoryAndPrice 'Home Goods', 10

--4. Stored Procedure with Insert Operation
--Create a stored procedure named InsertNewProduct that accepts parameters for ProductName, Category, Price, and StockQuantity and inserts a new product into the Products table.
CREATE PROCEDURE InsertNewProduct
    @ProductName NVARCHAR(100),
    @Category NVARCHAR(50),
    @Price INT,
    @StockQuantity INT
AS
BEGIN
    INSERT INTO Products (ProductName, Category, Price, StockQuantity)
    VALUES (@ProductName, @Category, @Price, @StockQuantity);
END;
EXEC InsertNewProduct 'Widget F','Offic Supplies',12.00,30

--5. Stored Procedure with Update Operation
--Create a stored procedure named UpdateCustomerEmail that accepts a CustomerID and a NewEmail parameter and updates the email address for the specified customer.
CREATE PROCEDURE UpdateCustomerEmail
    @CustomerID INT,
    @NewEmail NVARCHAR(100)
AS
BEGIN
    UPDATE Customers
    SET Email = @NewEmail
    WHERE CustomerID = @CustomerID;
END;
EXEC UpdateCustomerEmail 1,'amitupdated@gmail.com'

--6. Stored Procedure with Delete Operation
--Create a stored procedure named DeleteOrderByID that accepts an OrderID as a parameter and deletes the corresponding order from the Orders table.
CREATE PROCEDURE DeleteOrderByID
    @OrderID INT
AS
BEGIN
    DELETE FROM Orders
    WHERE OrderID = @OrderID;
END;
EXEC DeleteOrderByID 3

--7. Stored Procedure with Output Parameter
--Create a stored procedure named GetTotalProductsInCategory that accepts a Category parameter and returns the total number of products in that category using an output parameter.
CREATE PROCEDURE GetTotalProductsInCategory
    @Category NVARCHAR(50),
    @TotalProducts INT OUTPUT
AS
BEGIN
    SELECT @TotalProducts = COUNT(*)
    FROM Products
    WHERE Category = @Category;
END;
DECLARE @Total INT
EXEC GetTotalProductsInCategory 'Home Goods', @Total OUTPUT
SELECT @Total AS TotalProductsInCategory