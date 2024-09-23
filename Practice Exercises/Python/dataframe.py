import pandas as pd
data={
    "Name":["Amit","Priya","Vikram","Neha","Ravi"],
    "Age":[25,30,35,40,45],
    "City":["Mumbai","Delhi","Bangalore","Chennai","Pune"]
}

df=pd.DataFrame(data)
print(df)
#single column
print(df["Name"])
#multiple columns
print(df[["Name","Age"]])
#single row
print(df.iloc[0])
#multiple rows
print(df.iloc[0:2])

filtered=df[df["Age"]>30]
print(filtered)

df["Salary"]=[50000,60000,75000,80000,98000]
print(df)

newrow={"Name":"Surya","Age":25,"City":"Pondicherry","Salary":78000}
df.loc[len(df)]=newrow
print(df)

sorteddf=df.sort_values(by="Age",ascending=False)
print(sorteddf)

renamed=df.rename(columns={"Name":"Full Name","Age":"Years"})
print(renamed)

dropped=df.drop(columns=["City"])
print(dropped)

droprow=df.drop(index=2)
print(droprow)

df['Seniority']=df['Age'].apply(lambda x:'Senior' if x>35 else 'Junior')
print(df)

grouped=df.groupby("City")["Salary"].mean()
print(grouped)

def add_bonus(salary):
    return salary*1.50
df['Salary+Bonus']=df['Salary'].apply(add_bonus)
print(df)

df_new=pd.DataFrame({
    "Name":["Amit","Priya","Ravi"],
    "Bonus":[5000,6000,7000]
})

merged_left=pd.merge(df,df_new, on="Name", how="left")
print(merged_left)
merged_right=pd.merge(df,df_new, on="Name", how="right")
print(merged_right)

df_new2=pd.DataFrame({
    "Name":["Sonia","Rahul"],
    "Age":[29,31],
    "City":["Kolkata","Hyderabad"],
    "Salary":[58000,65000]
})
df_concat=pd.concat([df,df_new2],ignore_index=True)
print(df_concat)

salary_and_a=df[(df["Salary"]>=50000)&(df["Name"].str.startswith('A'))]
print(salary_and_a)