import json

data={"name":"Alice","age":30,"city":"new york"}
with open("C:/Users/USER/Documents/data2.json","w") as file:
    json.dump(data,file)

with open("C:/Users/USER/Documents/data2.json","r") as file:
    loaded_data=json.load(file)
    print(loaded_data)

