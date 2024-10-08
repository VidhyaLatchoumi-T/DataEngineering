CREATE TABLE user_dim (
    user_id INT PRIMARY KEY,
    user_name NVARCHAR(255),
    location NVARCHAR(255),
    age_group NVARCHAR(50)
);

CREATE TABLE transaction_fact (
    transaction_id INT PRIMARY KEY,
    user_id INT,
    amount INT,  
    transaction_time DATETIME,
    location NVARCHAR(255),
    fraud_label BIT,
    FOREIGN KEY (user_id) REFERENCES user_dim(user_id)
);

INSERT INTO user_dim (user_id, user_name, location, age_group) VALUES
(1, 'John Doe', 'New York', '30-40'),
(2, 'Jane Smith', 'Los Angeles', '20-30'),
(3, 'Alice Johnson', 'Chicago', '40-50'),
(4, 'Bob Brown', 'Houston', '30-40'),
(5, 'Carol White', 'Phoenix', '20-30');

INSERT INTO transaction_fact (transaction_id, user_id, amount, transaction_time, location, fraud_label) VALUES
(101, 1, 5000, '2024-08-28 10:15:00', 'New York', 0),
(102, 1, 12000, '2024-08-28 10:30:00', 'New York', 0),
(103, 2, 15000, '2024-08-28 11:00:00', 'Los Angeles', 1),
(104, 3, 2000, '2024-08-28 12:30:00', 'New York', 0),
(105, 4, 7500, '2024-08-28 13:45:00', 'Houston', 0),
(106, 5, 12000, '2024-08-28 14:10:00', 'Phoenix', 1),
(107, 4, 25000, '2024-08-29 12:45:00', 'Houston', 1),
(108, 5, 4000, '2024-08-29 13:55:00', 'New York', 0),
(109, 4, 25000, '2024-08-29 12:45:00', 'Houston', 1),
(110, 5, 4000, '2024-08-29 13:55:00', 'Phoenix', 0);

-- Query to detect suspicious transactions above a certain threshold
SELECT user_id, amount, transaction_time
FROM transaction_fact
WHERE amount > 10000
ORDER BY transaction_time DESC

--Query to Calculate Average Transaction Amount per User
SELECT user_id, AVG(amount) AS avg_transaction_amount
FROM transaction_fact
GROUP BY user_id;

--Query to identify multiple transactions from the same user in a short time
SELECT user_id, 
	COUNT(transaction_id) AS transaction_count, 
	MIN(transaction_time) AS first_transaction_time, 
	MAX(transaction_time) AS last_transaction_time
FROM transaction_fact
GROUP BY user_id
HAVING COUNT(transaction_id) > 1 AND DATEDIFF(MINUTE, MIN(transaction_time), MAX(transaction_time)) <= 60;

--Query to  Detect Transactions from Unusual Locations
SELECT tf.transaction_id, tf.user_id, tf.amount, tf.transaction_time, tf.location as transaction_location, ud.location as user_location
FROM transaction_fact tf
JOIN user_dim ud ON tf.user_id = ud.user_id
WHERE tf.location != ud.location;

--Query to Find the Most Frequent Locations for Fraudulent Transactions
SELECT location, COUNT(*) AS number_of_fraudulent_transactions
FROM transaction_fact
WHERE fraud_label = 1
GROUP BY location
ORDER BY number_of_fraudulent_transactions DESC
