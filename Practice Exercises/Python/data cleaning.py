import pandas as pd

df=pd.read_csv('sample_data.csv')
print(df)
import numpy as np
df.replace(r'^\s*$',np.nan, regex=True, inplace=True)
#number of null values across column
print(df.isnull().sum())
#null values across rows
print(df[df.isnull().any(axis=1)])

clean=df.dropna()
print(clean)
df.columns=df.columns.str.strip()
df['City']=df['City'].str.strip().replace('',np.nan)
df['City']=df['City'].fillna('Unknown')
df['Age']=pd.to_numeric(df['Age'].str.strip(),errors='coerce')
df['Age']=df['Age'].fillna(df['Age'].median())

df['Salary']=df['Salary'].fillna(df['Salary'].median())

print(df)

grouped=df.groupby('department')['salary'].mean().reset_index()
print(grouped)
