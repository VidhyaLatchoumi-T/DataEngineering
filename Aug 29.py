# *Exercise 1: Creating DataFrame from Scratch*
import pandas as pd
data={
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Category": ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    "Price": [80000, 1500, 20000, 3000, 40000],
    "Quantity": [10, 100, 50, 75, 30]
}
df=pd.DataFrame(data)
print(df)

# *Exercise 2: Basic DataFrame Operations*
print(df.head(3))
print(df.columns)
print(df.index)
print(df.describe())

# *Exercise 3: Selecting Data*
print(df[['Product', 'Price']])
print(df[df['Category'] == 'Electronics'])

# *Exercise 4: Filtering Data*
print(df[df['Price'] > 10000])
print(df[(df['Category'] == 'Accessories') & (df['Quantity'] > 50)])

# *Exercise 5: Adding and Removing Columns*
df['Total Value'] = df['Price'] * df['Quantity']
print(df)
df_drop = df.drop(columns=['Category'])
print(df_drop)

# *Exercise 6: Sorting Data*
print(df.sort_values(by='Price', ascending=False))
print(df.sort_values(by=['Quantity', 'Price'], ascending=[True, False]))

# *Exercise 7: Grouping Data*
grouped = df.groupby('Category')['Quantity'].sum()
print(grouped)
grouped_avg = df.groupby('Category')['Price'].mean()
print(grouped_avg)

# *Exercise 8: Handling Missing Data*
df.loc[1, 'Price'] = None
df.loc[3, 'Price'] = None
print(df)
df['Price']=df['Price'].fillna(df['Price'].mean())
print(df)
df = df[df['Quantity'] >= 50]
print(df)

# *Exercise 9: Apply Custom Functions*
df['Price'] = df['Price'].apply(lambda x: x * 1.05)
print(df)
df['Discounted Price'] = df['Price'] * 0.9
print(df)

# *Exercise 10: Merging DataFrames*
supplier_data = {
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Supplier": ['Dell', 'Logitech', 'Samsung', 'HP', 'Apple']
}
supplier_df = pd.DataFrame(supplier_data)
merged_df = pd.merge(df, supplier_df, on='Product')
print(merged_df)

# *Exercise 11: Pivot Tables*
pivot_table = df.pivot_table(values='Quantity', index='Product', columns='Category', aggfunc='sum')
print(pivot_table)

# *Exercise 12: Concatenating DataFrames*
store_a = pd.DataFrame({
    "Product": ['Laptop', 'Mouse', 'Monitor'],
    "Price": [80000, 1500, 20000],
    "Quantity": [5, 50, 25]
})
store_b = pd.DataFrame({
    "Product": ['Keyboard', 'Phone'],
    "Price": [3000, 40000],
    "Quantity": [40, 20]
})
combined_df = pd.concat([store_a, store_b])
print(combined_df)

# *Exercise 13: Working with Dates*
import numpy as np
date = pd.date_range(end=pd.Timestamp.today(), periods=5, freq='D')
df_dates = pd.DataFrame(date, columns=['Date'])
df_dates['Sales'] = np.random.randint(1000, 5000, size=(5))
print(df_dates)
total_sales = df_dates['Sales'].sum()
print("Total Sales:", total_sales)

# *Exercise 14: Reshaping Data with Melt*
df_sales = pd.DataFrame({
    "Product": ['Laptop', 'Phone', 'Monitor'],
    "Region": ['North', 'South', 'West'],
    "Q1_Sales": [25000, 40000, 15000],
    "Q2_Sales": [30000, 42000, 16000]
})
melted_df = pd.melt(df_sales, id_vars=['Product', 'Region'], var_name='Quarter', value_name='Sales')
print(melted_df)

# *Exercise 15: Reading and Writing Data*
df_from_csv = pd.read_csv('products.csv')
print(df_from_csv)
df_from_csv['New_Column'] = 'Example'
df_from_csv.to_csv('updated_products.csv', index=False)

# *Exercise 16: Renaming Columns*
df_rename = pd.DataFrame({
    "Prod": ['Laptop', 'Phone', 'Monitor'],
    "Cat": ['Electronics', 'Electronics', 'Electronics'],
    "Price": [80000, 40000, 20000],
    "Qty": [10, 30, 50]
})
df_rename.columns = ["Product", "Category", "Price", "Quantity"]
print(df_rename)

# *Exercise 17: Creating a MultiIndex DataFrame*
arrays = [
    ['Store_A', 'Store_A', 'Store_B', 'Store_B'],
    ['Laptop', 'Phone', 'Laptop', 'Monitor']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Store', 'Product'))
multiindex_df = pd.DataFrame({
    "Price": [80000, 40000, 85000, 22000],
    "Quantity": [5, 10, 8, 20]
}, index=index)
print(multiindex_df)

# *Exercise 18: Resample Time-Series Data*
date_rng = pd.date_range(end=pd.Timestamp.today(), periods=30, freq='D')
df_sales = pd.DataFrame(date_rng, columns=['Date'])
df_sales['Sales'] = np.random.randint(1000, 10000, size=(30))
print(df_sales)
weekly_sales = df_sales.resample('W', on='Date').sum()
print(weekly_sales)

# *Exercise 19: Handling Duplicates*
df_duplicates = pd.DataFrame({
    "Product": ['Laptop', 'Phone', 'Monitor', 'Laptop', 'Phone'],
    "Price": [80000, 40000, 20000, 80000, 40000],
    "Quantity": [10, 30, 50, 10, 30]
})
df_cleaned = df_duplicates.drop_duplicates()
print(df_cleaned)

# *Exercise 20: Correlation Matrix*
df_corr = pd.DataFrame({
    "Height": [150, 160, 170, 180, 190],
    "Weight": [55, 65, 75, 85, 95],
    "Age": [25, 30, 35, 40, 45],
    "Income": [30000, 40000, 50000, 60000, 70000]
})
corr_matrix = df_corr.corr()
print(corr_matrix)

# *Exercise 21: Cumulative Sum and Rolling Windows*
date = pd.date_range(end=pd.Timestamp.today(), periods=30, freq='D')
df_sales = pd.DataFrame(date, columns=['Date'])
df_sales['Sales'] = np.random.randint(1000, 10000, size=(30))
df_sales['Cumulative Sales'] = df_sales['Sales'].cumsum()
print(df_sales)
df_sales['Rolling Avg'] = df_sales['Sales'].rolling(window=7).mean()
print(df_sales)

# *Exercise 22: String Operations*
df_names = pd.DataFrame({
    "Names": ["John Doe", "Jane Smith", "Sam Brown"]
})
df_names[['First Name', 'Last Name']] = df_names['Names'].str.split(' ', expand=True)
print(df_names)
df_names['First Name'] = df_names['First Name'].str.upper()
print(df_names)

# **Exercise 23: Conditional Selections with np.where**
import numpy as np
df_employees = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Age": [45, 34, 50, 28],
    "Department": ["HR", "Finance", "IT", "Sales"]
})
df_employees['Status'] = np.where(df_employees['Age'] >= 40, "Senior", "Junior")
print(df_employees)

# *Exercise 24: Slicing DataFrames*
df_slicing = pd.DataFrame({
    "Products": ["Laptop", "Phone", "Monitor", "Keyboard", "Mouse"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Sales": [100000, 50000, 30000, 12000, 8000],
    "Profit": [20000, 15000, 7000, 2000, 1000]
})
print(df_slicing.head(10))
print(df_slicing[df_slicing['Category'] == 'Electronics'])
print(df_slicing[df_slicing['Sales'] > 50000][['Sales', 'Profit']])

# *Exercise 25: Concatenating DataFrames Vertically and Horizontally*
df_store_a = pd.DataFrame({
    "Employee": ["Alice", "Bob"],
    "Age": [45, 34],
    "Salary": [70000, 50000]
})
df_store_b = pd.DataFrame({
    "Employee": ["Charlie", "David"],
    "Age": [50, 28],
    "Salary": [80000, 40000]
})
combined_df = pd.concat([df_store_a, df_store_b])
print(combined_df)
df_emp_dept = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "Finance", "IT", "Sales"]
})
df_emp_salary = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Salary": [70000, 50000, 80000, 40000]
})
combined_df_horizontal = pd.merge(df_emp_dept, df_emp_salary, on='Employee')
print(combined_df_horizontal)

# *Exercise 26: Exploding Lists in DataFrame Columns*
df_explode = pd.DataFrame({
    "Product": ["Laptop", "Phone"],
    "Features": [["Feature1", "Feature2"], ["Feature3", "Feature4"]]
})
df_exploded = df_explode.explode('Features')
print(df_exploded)

# *Exercise 27: Using .map() and .applymap()*
df_map = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Monitor"],
    "Price": [80000, 40000, 20000],
    "Quantity": [10, 30, 50]
})
df_map['Price'] = df_map['Price'].map(lambda x: x * 1.1)
print(df_map)
df_map = df_map.map(lambda x: f"{x:.2f}" if isinstance(x, (int, float)) else x)
print(df_map)

# **Exercise 28: Combining groupby() with apply()**
df_group_apply = pd.DataFrame({
    "City": ["New York", "New York", "Los Angeles", "Los Angeles"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone"],
    "Sales": [100000, 50000, 80000, 60000],
    "Profit": [20000, 15000, 25000, 18000]
})
df_group_apply['Profit Margin'] = df_group_apply['Profit'] / df_group_apply['Sales']
city_grouped = df_group_apply.groupby('City').apply(lambda x: x)
print(city_grouped)

# *Exercise 29: Creating a DataFrame from Multiple Sources*
df_csv = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Monitor"],
    "Price": [80000, 40000, 20000]
})
json_data = {
    "Product": ["Laptop", "Phone", "Monitor"],
    "Quantity": [10, 30, 50]
}
df_json = pd.DataFrame(json_data)
dict_data = {
    "Product": ["Laptop", "Phone", "Monitor"],
    "Supplier": ["Dell", "Apple", "Samsung"]
}
df_dict = pd.DataFrame(dict_data)
consolidated_df = pd.merge(pd.merge(df_csv, df_json, on='Product'), df_dict, on='Product')
print(consolidated_df)

# *Exercise 30: Dealing with Large Datasets*
date_rng = pd.date_range(start='1/1/2023', periods=1000000, freq='min')
df_large = pd.DataFrame(date_rng, columns=['Date'])
df_large['Transaction ID'] = range(1, 1000001)
df_large['Customer'] = ['Customer_' + str(i) for i in range(1, 1000001)]
df_large['Product'] = ['Product_' + str(i % 100) for i in range(1, 1000001)]
df_large['Amount'] = np.random.randint(1, 1000, size=(1000000))

chunk_size = 100000
chunks = [df_large[i:i + chunk_size] for i in range(0, df_large.shape[0], chunk_size)]

total_sales_per_chunk = [chunk['Amount'].sum() for chunk in chunks]

summary_df = pd.DataFrame({
    'Chunk': range(1, len(chunks) + 1),
    'Total Sales': total_sales_per_chunk
})

print(summary_df)