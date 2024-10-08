import pandas as pd

transaction_data = pd.read_csv("C:/Users/USER/Desktop/Python-Data Engineering/Project/ECommerce/transaction_fact.csv")

#Data Preprocessing
# correct date and time format
transaction_data['transaction_time'] = pd.to_datetime(transaction_data['transaction_time'])

# normalize the transaction amounts
transaction_data['normalized_amount'] = (transaction_data['transaction_amount'] - transaction_data['transaction_amount'].mean()) /transaction_data['transaction_amount'].std()

#Feature engineering
# transaction frequency per user
transaction_data['transaction_frequency'] = transaction_data.groupby('user_id') ['transaction_id'].transform('count')

# suspicious transactions
transaction_data['is_suspicious'] = transaction_data['transaction_amount'] > 1000

# rolling average of the last 5 transactions
transaction_data['rolling_avg_amount'] = transaction_data['transaction_amount'].rolling(window=5).mean()

# Display the processed transaction data
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(transaction_data)


