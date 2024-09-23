# *Exercise 1: Handling Missing Values*
import pandas as pd
data = {
    "Name": ["Amit", "Neha", "Raj", "Priya"],
    "Age": [28, None, 35, 29],
    "City": ["Delhi", "Mumbai", None, "Chennai"]
}
df = pd.DataFrame(data)
print(df)
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)
df_dropped=df.dropna()
print(df_dropped)

# *Exercise 2: Adding and Removing Columns*
df['Salary']=[50000,60000,70000,65000]
df_city_drop=df.drop(columns='City')
print(df_city_drop)

# *Exercise 7: Sorting Data*
df.sort_values(by='Age',inplace=True)
print(df)
df.sort_values(by=['City', 'Age'], ascending=[True, False], inplace=True)
print(df)

# *Exercise 8: Grouping and Aggregation*
age_city=df.groupby('City')['Age'].mean()
print(age_city)
count=df.groupby(['City','Age']).count()
print(count)

# *Exercise 9: Merging DataFrames*
df1 = pd.DataFrame({
       "Name": ["Amit", "Neha", "Raj"],
       "Department": ["HR", "IT", "Finance"]
   })
df2 = pd.DataFrame({
       "Name": ["Neha", "Raj", "Priya"],
       "Salary": [60000, 70000, 65000]
   })

merge=pd.merge(df1,df2,on="Name",how="inner")
merge_left=pd.merge(df1,df2,on="Name",how="left")
print(merge)
print(merge_left)
