import pandas as pd
df=pd.read_csv('employee.csv')
#print(df)

print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())

high_salary_df=df[df[' Salary']>80000]
print(high_salary_df)

sorted_df=df.sort_values(by=' Age',ascending=False)
print(sorted_df)