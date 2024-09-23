import pandas as pd
df=pd.read_json('employees.json')
print(df)

df['Bonus']=df['Salary']*0.10
print(df)

df.to_json('emp_with_bonus.json',orient='records', lines=True)