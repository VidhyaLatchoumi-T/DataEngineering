# Exercise 1: Create a Dictionary
person={
    "Name":"Alice",
    "Age":"25",
    "City":"NewYork"
}
print(person)

# Exercise 2: Access Dictionary Elements
Name=person["Name"]
City=person["City"]
print("Name: ",Name)
print("City: ",City)

# Exercise 3: Add and Modify Elements
person["Email"]="alice@example.com"
person["Age"]=26
print(person)

# Exercise 4: Remove Elements
del person["City"]
print(person)

# Exercise 5: Check if a Key Exists
if "Email" in person:
    print("Email present")
else:
    print("Email not present")
if "Phone" in person:
    print("Phone present")
else:
    print("Phone not present")

# Exercise 6: Loop Through a Dictionary
for key, values in person.items():
    print(key,": ",values)
for key in person:
    print(key)
for value in person.values():
    print(value)

# Exercise 7: Nested Dictionary
employees = {
       101: {"name": "Bob", "job": "Engineer"},
       102: {"name": "Sue", "job": "Designer"},
       103: {"name": "Tom", "job": "Manager"}
   }
print(employees)
print(employees[102])
employees[104]={"name":"Linda", "job":"HR"}
print(employees)

# Exercise 8: Dictionary Comprehension
squares={x: x**2 for x in range(1,6)}
print(squares)

# Exercise 9: Merge Two Dictionaries
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
dict1.update(dict2)
print(dict1)

# Exercise 10: Default Dictionary Values
let_to_num={"a":1,"b":2,"c":3}
print(let_to_num.get("b"))
print(let_to_num.get("d",0))

# Exercise 11: Dictionary from Two Lists
keys=["name","age","city"]
values=["Eve",29,"San Francisco"]
person_new=dict(zip(keys,values))
print(person_new)

# Exercise 12: Count Occurrences of Words
sentence = "the quick brown fox jumps over the lazy dog the fox"
count={}
for word in sentence.split():
    count[word]=count.get(word,0)+1
print(count)
