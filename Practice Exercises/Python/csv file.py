import csv
data=[["Name","Age"],["Alice",25],["Bob",30]]
with open("C:/Users/USER/Documents/data.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)

with open("C:/Users/USER/Documents/data.csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
