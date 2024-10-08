create database ECommerce
CREATE TABLE user_dim (
    user_id INT PRIMARY KEY, 
    user_name VARCHAR(255) NOT NULL, 
    location VARCHAR(255)
);

CREATE TABLE transaction_fact (
    transaction_id INT PRIMARY KEY, 
    user_id INT FOREIGN KEY REFERENCES user_dim(user_id), 
    transaction_amount DECIMAL(10, 2) NOT NULL, 
    transaction_time DATETIME NOT NULL, 
    payment_method VARCHAR(50) NOT NULL, 
    location VARCHAR(255) NOT NULL,
    fraud_label BIT
);

--Inserting Data

INSERT INTO user_dim (user_id, user_name, location) VALUES
(1, 'Alice Johnson', 'New York'),
(2, 'Bob Smith', 'Los Angeles'),
(3, 'Charlie Brown', 'Chicago'),
(4, 'Diana Prince', 'Houston'),
(5, 'Eve Black', 'San Francisco'),
(6, 'Frank White', 'Miami'),
(7, 'Grace Green', 'Seattle'),
(8, 'Henry Adams', 'Denver'),
(9, 'Ivy Blue', 'Boston'),
(10, 'Jack Grey', 'Atlanta');

INSERT INTO transaction_fact (transaction_id, user_id, transaction_amount, transaction_time, payment_method, location, fraud_label) VALUES
(201, 1, 300.00, '2024-08-15 10:30:00', 'Credit Card', 'New York', 0),
(202, 2, 1500.00, '2024-08-16 12:45:00', 'PayPal', 'Los Angeles', 0),
(203, 3, 450.00, '2024-08-17 09:20:00', 'Debit Card', 'Chicago', 0),
(204, 4, 2200.00, '2024-08-18 14:00:00', 'Credit Card', 'Houston', 0),
(205, 5, 50.00, '2024-08-19 16:10:00', 'Credit Card', 'San Francisco', 0),
(206, 6, 900.00, '2024-08-20 11:30:00', 'Bank Transfer', 'Miami', 0),
(207, 7, 700.00, '2024-08-21 13:50:00', 'Debit Card', 'Seattle', 0),
(208, 8, 1800.00, '2024-08-22 10:10:00', 'PayPal', 'Denver', 0),
(209, 9, 80.00, '2024-08-23 15:00:00', 'Credit Card', 'Boston', 0),
(210, 10, 2500.00, '2024-08-24 17:20:00', 'Bank Transfer', 'Atlanta', 0),
(211, 1, 600.00, '2024-08-25 10:00:00', 'Credit Card', 'New York', 0),
(212, 3, 1200.00, '2024-08-26 11:30:00', 'Credit Card', 'Chicago', 0),
(213, 4, 75.00, '2024-08-27 14:50:00', 'Debit Card', 'Houston', 0),
(214, 2, 300.00, '2024-08-28 13:15:00', 'Bank Transfer', 'Los Angeles', 0),
(215, 6, 500.00, '2024-08-29 09:40:00', 'Credit Card', 'Miami', 0),
(216, 9, 1000.00, '2024-08-29 12:00:00', 'PayPal', 'Boston', 0),
(217, 10, 150.00, '2024-08-29 13:30:00', 'Debit Card', 'Atlanta', 0),
(218, 7, 220.00, '2024-08-29 14:10:00', 'Credit Card', 'Seattle', 0),
(219, 8, 1700.00, '2024-08-29 15:45:00', 'Bank Transfer', 'Denver', 0),
(220, 5, 200.00, '2024-08-29 16:20:00', 'Debit Card', 'San Francisco', 0);

--Query to Find the Fraudulent Transaction with a Threshold

SELECT user_id, transaction_amount, transaction_time
FROM transaction_fact
WHERE transaction_amount > 1000
ORDER BY transaction_time DESCUPDATE transaction_fact
SET fraud_label = 1
WHERE transaction_id IN (
    SELECT transaction_id
    FROM transaction_fact
    WHERE transaction_amount > 1000
);
--Query to Find the Total Transaction Amount for Each User:

SELECT user_id, SUM(transaction_amount) AS total_spent
FROM transaction_fact
GROUP BY user_id
ORDER BY total_spent DESC

--Query to Count the Number of Fraudulent Transactions and the Total Amount Involved

SELECT COUNT(*) AS total_fraudulent_transactions, SUM(transaction_amount) AS total_fraudulent_amount
FROM transaction_fact
WHERE fraud_label = 1

--Query to Find Users with Multiple Fraudulent Transactions

SELECT user_id, COUNT(*) AS number_of_fraudulent_transactions
FROM transaction_fact
WHERE fraud_label = 1
GROUP BY user_id
HAVING COUNT(*) > 1
ORDER BY number_of_fraudulent_transactions DESC

--Query to Analyze Fraudulent Transactions by Payment Method

SELECT payment_method, COUNT(*) AS number_of_fraudulent_transactions, SUM(transaction_amount) AS total_fraudulent_amount
FROM transaction_fact
WHERE fraud_label = 1
GROUP BY payment_method
ORDER BY total_fraudulent_amount DESC

--Query to Find the Most Frequent Locations for Fraudulent Transactions

SELECT location, COUNT(*) AS number_of_fraudulent_transactions
FROM transaction_fact
WHERE fraud_label = 1
GROUP BY location
ORDER BY number_of_fraudulent_transactions DESC

--Query to Retrieve Recent Fraudulent Transactions (in the past 30 Days)

SELECT transaction_id, user_id, transaction_amount, transaction_time, payment_method, location
FROM transaction_fact
WHERE fraud_label = 1 AND transaction_time >= DATEADD(DAY, -30, GETDATE())
ORDER BY transaction_time DESC