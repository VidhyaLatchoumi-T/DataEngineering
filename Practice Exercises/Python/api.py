import requests

response=requests.get("https://dummyjson.com/products/1")
print(response.json())

import pandas as pd
data = {
    "Name": ["Amit", "Neha", "Raj", "Priya"],
    "Age": [28, None, 35, 29],
    "City": ["Delhi", "Mumbai", None, "Chennai"],
    "Temperature": [30, 32, None, 38]
}
df = pd.DataFrame(data)

print("Original DataFrame with missing values:")
print(df)

df['Age']=df['Age'].fillna(df['Age'].mean())
print("\nDataFrame after filling missing 'Age' with the mean:")
print(df)

df_cleaned = df.dropna()
print("\nDataFrame after dropping rows with any missing values:")
print(df_cleaned)

df['Temperature'] = df['Temperature'].interpolate()
print("\nDataFrame after interpolating missing 'Temperature':")
print(df)

df.dropna(inplace=True)
print("\nDataFrame after dropping rows using inplace parameter:")
print(df_cleaned)


