empty_dict={}
person={
    "name": "Mark",
    "age": 30,
    "email": "mark@abc.in"
}
print(empty_dict)
print(person)

name=person["name"]
age=person["age"]
print("Name: ",name)
print("Age: ",age)

person["age"]=31
person["email"]="mark_new@abc.in"
print(person)

person["address"]="123 Main St"
print(person)
del person["email"]
print(person)

keys=person.keys()
values=person.values()
items=person.items()
print("Keys:",keys)
print("Values:",values)
print("Items:",items)

for key in person.keys():
    print(key)
for value in person.values():
    print(value)
for key,value in person.items():
    print(key,":",value)