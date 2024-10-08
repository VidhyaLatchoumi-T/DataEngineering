import pandas as pd

transactions = pd.read_csv("C:/Users/USER/Desktop/Python-Data Engineering/Project/FinancialTransactions/transaction_data.csv")

# Convert transaction time to datetime
transactions['transaction_time'] = pd.to_datetime(transactions['transaction_time'])

# Calculate time difference between consecutive transactions
transactions['time_diff'] = transactions.groupby('user_id')['transaction_time'].diff().dt.total_seconds()

# Calculate the frequency of transactions per user
transactions['transaction_frequency'] = transactions.groupby('user_id')['transaction_time'].transform('count')

# Detect large jumps in transaction amounts
transactions['amount_diff'] = transactions.groupby('user_id')['transaction_amount'].diff().fillna(0).abs()

# Normalize transaction amounts
transactions['amount_normalized'] = (transactions['transaction_amount'] - transactions['transaction_amount'].mean()) / transactions['transaction_amount'].std()

# Deviation from typical user behavior
transactions['deviation_from_mean'] = abs(transactions['transaction_amount'] - transactions.groupby('user_id')['transaction_amount'].transform('mean'))

# Display the first few rows of the transformed dataset
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(transactions)