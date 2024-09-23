INSERT INTO Employees (EmployeeID, FirstName, LastName, Position, Department, HireDate) VALUES
(1, 'Amit', 'Sharma', 'Software Engineer', 'IT', '2022-01-15'),
(2, 'Priya', 'Mehta', 'Project Manager', 'Operations', '2023-02-20'),
(3, 'Raj', 'Patel', 'Business Analyst', 'Finance', '2021-06-30'),
(4, 'Sunita', 'Verma', 'HR Specialist', 'HR', '2019-08-12'),
(5, 'Vikram', 'Rao', 'Software Engineer', 'IT', '2021-03-18'),
(6, 'Anjali', 'Nair', 'HR Manager', 'HR', '2020-05-14'),
(7, 'Rohan', 'Desai', 'Finance Manager', 'Finance', '2022-11-25'),
(8, 'Sneha', 'Kumar', 'Operations Coordinator', 'Operations', '2023-07-02'),
(9, 'Deepak', 'Singh', 'Data Scientist', 'IT', '2022-08-05'),
(10, 'Neha', 'Gupta', 'Business Analyst', 'Finance', '2020-10-10');

select * from Employees

select * from Employees 
where Department='IT';

select * from Employees 
where HireDate > '2022-01-01';

select * from Employees 
where Department='HR' or Department='Finance';

select * from Employees 
where Position='Software Engineer' and HireDate>'2021-01-01';

select * from Employees 
where LastName like 'S%';

select * from Employees 
where FirstName like '%n%';

select count(*) from Employees 

select top 1 HireDate from Employees 
order by HireDate ASC


select ProductName, Category,Price
from Products
where ProductName LIKE 'S%'
select ProductName as Name, Price as Cost, 
StockQuantity as Quantity
from Products
where ProductName LIKE '%Phone%'

select p1.ProductName as Product1,
p2.ProductName as Product2,p1.Category
from Products p1
inner join Products p2
on p1.Category=p2.Category
and p1.ProductId<>p2.ProductId

select p.Category, SUM(o.Quantity) as totalquantity
from orders o
inner join products p 
on o.productid=p.productid
group by p.category

select p.Category, SUM(o.Quantity) as totalquantity
from orders o
inner join products p 
on o.productid=p.productid
group by p.category
having sum(o.quantity)>3










select p.Category, SUM(o.Quantity) as totalquantity
from orders o
inner join products p 
on o.productid=p.productid
group by p.category
select sum(quantity)as overall from orders 

select p.productid, p.ProductName , count(o.orderid) as orderno
from orders o
join Products p 
on o.productid=p.productid
group by p.productname
having count(o.orderid)>5

select distinct p.productid,p.productname
from orders o
join Products p 
on o.productid=p.productid

select distinct productid,productname,price
from Products
where price>(
select max(price) from products where category='Accessories')

select distinct productid,productname,price
from Products
where price>(
select max(price) from products where category='Accessories')




SELECT ProductName, UPPER(ProductName) AS ProductNameUpperCase FROM Products;

SELECT ProductName, LOWER (ProductName) AS ProductNameLowerCase FROM Products;

SELECT ProductName, SUBSTRING (ProductName, 1, 3) AS Short Name FROM Products;

SELECT ProductName, LEN (ProductName) AS NameLength FROM Products;

SELECT ProductName, REPLACE (ProductName, 'Phone', 'Device') AS Updated ProductName FROM Products;

SELECT ProductName, LTRIM(RTRIM(ProductName)). AS Trimmed ProductName FROM Products;

SELECT ProductName, CHARINDEX('e', ProductName) AS PositionofE FROM Products;

SELECT ProductName, Category, CONCAT (Productiame, , Category) AS ProductDetails FROM Products;

SELECT ProductName, LEFT (ProductName, 5) AS ShortName FROM Products;

SELECT ProductName, RIGHT (ProductName, 3) AS LastCharacters FROM Products;

SELECT ProductName, REVERSE (ProductName) AS ReversedName FROM Products;

SELECT ProductName, FORMAT (Price, '112') AS FormattedPrice FROM Products,

SELECT ProductName, REPLICATE (ProductName, 3 AS Repeated ProductName FROM Products;