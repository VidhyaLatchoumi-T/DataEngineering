CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(100)
);
INSERT INTO Customers (CustomerID, CustomerName, City) VALUES
(1, 'John Doe', 'New York'),
(2, 'Jane Smith', 'Los Angeles'),
(3, 'Michael Brown', 'Chicago'),
(4, 'Emily Davis', 'Houston'),
(5, 'James Wilson', 'Phoenix'),
(6, 'Sophia Johnson', 'Philadelphia'),
(7, 'Daniel Taylor', 'San Antonio'),
(8, 'Emma Moore', 'San Diego'),
(9, 'Olivia Garcia', 'Dallas'),
(10, 'Ava Martinez', 'Mumbai');
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderAmount DECIMAL(10, 2),
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
INSERT INTO Orders (OrderID, CustomerID, OrderAmount, OrderDate) VALUES
(1, 1, 250.00, '2023-01-15'),
(2, 2, 300.00, '2023-02-10'),
(3, 1, 450.00, '2023-03-05'),
(4, 3, 150.00, '2023-04-22'),
(5, 4, 700.00, '2023-05-30'),
(6, 5, 900.00, '2023-06-18'),
(7, 2, 1200.00, '2023-07-14'),
(8, 6, 300.00, '2023-08-01'),
(9, 7, 800.00, '2023-08-12'),
(10, 8, 500.00, '2023-09-05'),
(11, 9, 400.00, '2023-10-10'),
(12, 10, 1300.00, '2023-11-20'),
(13, 10, 700.00, '2023-12-25'),
(14, 1, 600.00, '2023-12-31'),
(15, 3, 500.00, '2024-01-15'),
(16, 5, 1100.00, '2024-02-10');
--### *1. Filter and Aggregate on Join Results using SQL*
--- Task: Join the Orders and Customers tables to find the total order amount per customer and filter out customers who have spent less than $1,000.
SELECT C.CustomerID, C.CustomerName,SUM(O.OrderAmount) AS TotalSpent
FROM Customers C
JOIN Orders O 
ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CustomerName
HAVING SUM(O.OrderAmount) <= 1000;

--### *2. Cumulative Aggregations and Ranking in SQL Queries*
--- Task: Create a cumulative sum of the OrderAmount for each customer to track the running total of how much each customer has spent.
SELECT CustomerID,OrderAmount, 
SUM(OrderAmount) OVER (PARTITION BY CustomerID ORDER BY OrderAmount) AS RunningTotal
FROM Orders O;

--### *3. OVER and PARTITION BY Clause in SQL Queries*
--- Task: Rank the customers based on the total amount they have spent, partitioned by city.
SELECT C.CustomerID, C.CustomerName, C.City, SUM(O.OrderAmount) AS TotalSpent,
    RANK() OVER (PARTITION BY C.City ORDER BY SUM(O.OrderAmount) DESC ) AS CustomerRank
FROM Customers C
JOIN Orders O 
ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CustomerName,C.City;

--### *4. Total Aggregation using OVER and PARTITION BY in SQL Queries*
--- Task: Calculate the total amount of all orders (overall total) and the percentage each customer's total spending contributes to the overall total.
WITH CustomerTotals AS (
    SELECT C.CustomerID, C.CustomerName, SUM(O.OrderAmount) AS TotalSpent
    FROM Customers C
    JOIN Orders O 
    ON C.CustomerID = O.CustomerID
    GROUP BY C.CustomerID, C.CustomerName
)
SELECT CustomerID, CustomerName, TotalSpent,
    SUM(TotalSpent) OVER () AS OverallTotal,
    (TotalSpent * 100.0) / SUM(TotalSpent) OVER () AS PercentageOfTotal
FROM CustomerTotals;

--### *5. Ranking in SQL*
--- Task: Rank all customers based on the total amount they have spent, without partitioning.
SELECT C.CustomerID, C.CustomerName, SUM(O.OrderAmount) AS TotalSpent,
    RANK() OVER (ORDER BY SUM(O.OrderAmount) DESC) AS CustomerRank
FROM Customers C
JOIN Orders O 
ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CustomerName;

--Here are additional tasks that build on the concepts of filtering, aggregating, ranking, and window functions in SQL:

--### *6. Task: Calculate the Average Order Amount per City*
--- Task: Write a query that joins the Orders and Customers tables, calculates the average order amount for each city, and orders the results by the average amount in descending order.
SELECT C.City, AVG(O.OrderAmount) AS AverageAmount
FROM Customers C
JOIN Orders O 
ON C.CustomerID = O.CustomerID
GROUP BY C.City
ORDER BY AverageAmount DESC;

--### *7. Task: Find Top N Customers by Total Spending*
--- Task: Write a query to find the top 3 customers who have spent the most, using ORDER BY and LIMIT.
SELECT TOP 3  C.CustomerID, C.CustomerName, SUM(O.OrderAmount) AS TotalSpent
FROM Customers C
JOIN Orders O 
ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CustomerName
ORDER BY TotalSpent DESC;

--### *8. Task: Calculate Yearly Order Totals*
--- Task: Write a query that groups orders by year (using OrderDate), calculates the total amount of orders for each year, and orders the results by year.
SELECT YEAR(O.OrderDate) AS OrderYear, SUM(O.OrderAmount) AS TotalAmount
FROM Orders O
GROUP BY YEAR(O.OrderDate)
ORDER BY OrderYear ASC;

--### *9. Task: Calculate the Rank of Customers by Total Order Amount*
--- Task: Write a query that ranks customers by their total spending, but only for customers located in "Mumbai". The rank should reset for each customer in "Mumbai".
SELECT C.CustomerID, C.CustomerName, C.City, 
    SUM(O.OrderAmount) AS TotalSpent,
    RANK() OVER (ORDER BY SUM(O.OrderAmount) DESC) AS CustomerRank
FROM Customers C
JOIN Orders O 
ON C.CustomerID = O.CustomerID
WHERE C.City = 'Mumbai'
GROUP BY C.CustomerID, C.CustomerName, C.City;

--### *10. Task: Compare Each Customer's Total Order to the Average Order Amount*
--- Task: Write a query that calculates each customer's total order amount and compares it to the average order amount for all customers.
WITH CustomerTotals AS (
    SELECT C.CustomerID, C.CustomerName, 
        SUM(O.OrderAmount) AS TotalSpent
    FROM Customers C
    JOIN Orders O 
    ON C.CustomerID = O.CustomerID
    GROUP BY C.CustomerID, C.CustomerName
)
SELECT CustomerID, 
    CustomerName, 
    TotalSpent,
    AVG(TotalSpent) OVER () AS AverageOrderAmount,
    TotalSpent - AVG(TotalSpent) OVER () AS DifferenceFromAverage
FROM CustomerTotals;


