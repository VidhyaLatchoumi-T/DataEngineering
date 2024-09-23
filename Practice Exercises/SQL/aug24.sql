CREATE TABLE Customers (
CustomerID INT PRIMARY KEY,
FirstName NVARCHAR(50),
LastName NVARCHAR(50),
Email NVARCHAR(100),
PhoneNumber VARCHAR(15));

INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber)
VALUES
(1, 'Amit', 'Sharma', 'amit.sharma@example.com', '9876543210'),
(2, 'Priya', 'Mehta', 'priya.mehta@example.com', '8765432109'),
(3, 'Rohit', 'Kumar', 'rohit.kumar@example.com', '7654321098'),
(4, 'Neha', 'Verma', 'neha.verma@example.com', '6543210987'),
(5, 'Siddharth', 'Singh', 'siddharth.singh@example.com', '5432109876'),
(6, 'Asha', 'Rao', 'asha.rao@example.com', '4321098765');

UPDATE Customers
SET FirstName=LTRIM(RTRIM(LOWER(FirstName))),
	LastName=LTRIM(RTRIM(LOWER(LastName)));

	select * from Customers where FirstName LIKE 'A%'
	select * from Customers where PhoneNumber LIKE '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]'
	select * from Customers where LastName LIKE '_____'

SELECT CustomerID, OrderID, TotalAmount,
SUM(TotalAmount) OVER(PARTITION BY CustomerID ORDER BY OrderDate)
AS RunningTotal
FROM Orders;

CREATE TABLE Employees1 ( 
EmployeeID INT PRIMARY KEY IDENTITY(1,1), 
EmployeeName VARCHAR(100), 
ManagerID INT NULL );

INSERT INTO Employees1 (EmployeeName, ManagerID)
VALUES 
('Amit Sharma', NULL),  -- Top manager
('Priya Mehta', 1),     -- Reports to Amit
('Rohit Kumar', 1),     -- Reports to Amit
('Neha Verma', 2),      -- Reports to Priya
('Siddharth Singh', 2), -- Reports to Priya
('Asha Rao', 3);        -- Reports to Rohit
 
INSERT INTO Employees1 (EmployeeName, ManagerID)
VALUES 
('Vikram Gupta', 4),  -- Reports to Neha
('Rajesh Patel', 5);  -- Reports to Siddharth

 
  WITH RecursiveEmployeeCTE AS (
    SELECT EmployeeID, ManagerID, EmployeeName 
    FROM  Employees1 
    WHERE ManagerID IS NULL
    UNION ALL
    SELECT e.EmployeeID,  e.ManagerID,  e.EmployeeName 
    FROM  Employees1 e 
    INNER JOIN RecursiveEmployeeCTE r ON e.ManagerID = r.EmployeeID
)
SELECT * FROM RecursiveEmployeeCTE;

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Category VARCHAR(50),
    Amount DECIMAL(10, 2),
    SaleDate DATE
);
 
INSERT INTO Sales (SaleID, ProductID, Category, Amount, SaleDate) 
VALUES 
(1, 101, 'Electronics', 1500.00, '2024-01-15'),
(2, 102, 'Furniture', 800.00, '2024-01-16'),
(3, 103, 'Electronics', 2000.00, '2024-01-17'),
(4, 104, 'Electronics', 1200.00, '2024-02-01'),
(5, 105, 'Furniture', 900.00, '2024-02-03');

SELECT Category, SUM(Amount) AS TotalSales
FROM Sales
GROUP BY ROLLUP(Category);

CREATE TABLE Orders2 (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderAmount DECIMAL(10, 2),
    OrderDate DATE
);
 
INSERT INTO Orders2 (OrderID, CustomerID, OrderAmount, OrderDate)
VALUES 
(1, 1, 500.00, '2024-01-15'),
(2, 2, 700.00, '2024-01-16'),
(3, 1, 300.00, '2024-01-17'),
(4, 3, 1200.00, '2024-02-01'),
(5, 2, 900.00, '2024-02-03');

SELECT DISTINCT o1.CustomerID
FROM Orders2 o1
WHERE(
SELECT COUNT(*)
FROM Orders2 o2
WHERE o2.CustomerID=o1.CustomerID
)>1


CREATE TABLE ProductSales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Amount DECIMAL(10, 2),
    SaleDate DATE
);
 
INSERT INTO ProductSales (SaleID, ProductID, Amount, SaleDate)
VALUES 
(1, 101, 1500.00, '2024-01-15'),
(2, 102, 800.00, '2024-01-16'),
(3, 103, 2000.00, '2024-01-17'),
(4, 104, 1200.00, '2024-02-01'),
(5, 105, 900.00, '2024-02-03');

CREATE VIEW TotalSalesByProduct
WITH SCHEMABINDING
AS
SELECT ProductID, SUM(Amount) AS TotalSales
FROM dbo.ProductSales
GROUP BY ProductID;

SELECT * FROM TotalSalesByProduct