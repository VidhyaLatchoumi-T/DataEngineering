# Exercise 1: List Operations
numbers=[1,2,3,4,5]
numbers.append(6)
numbers.remove(3)
numbers.insert(0,0)
print(numbers)

# Exercise 2: Tuple Operations
coordinates=(10.0,20.0,30.0)
print(coordinates[1])
##coordinates[2]=40.0 #(throws error)TypeError: 'tuple' object does not support item assignment

# Exercise 3: Set Operations
fruits={"apple","banana","cherry"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)

if "cherry" in fruits:
    print("Cherry present")
else:
    print("Cherry not present")

citrus={"orange","lemon","lime"}
unionset=fruits.union(citrus)
print(unionset)
intersectionset=fruits.intersection(citrus)
print(intersectionset)

# Exercise 4: Dictionary Operations
person={
    "name":"John",
    "age":30,
    "city":"new york"
}
print(person["name"])
person["age"]=31
person["email"]="john@example.com"
del person["city"]
print(person)

# Exercise 5: Nested Dictionary
school = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 78, "Science": 92},
    "Charlie": {"Math": 95, "Science": 88}
}
print(school["Alice"]["Math"])
school["David"]={"Math": 80, "Science": 89}
school["Bob"]["Science"]=95
print(school)

# Exercise 6: List Comprehension
numbers = [1, 2, 3, 4, 5]
square = [x**2 for x in numbers]
print(square)

# Exercise 7: Set Comprehension
num=[1,2,3,4,5]
squared_set = {x**2 for x in num}
print(squared_set)

# Exercise 8: Dictionary Comprehension
cubes_dict = {x: x**3 for x in range(1, 6)}
print(cubes_dict)

# Exercise 9: Combining Collections
keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]
combined = dict(zip(keys, values))
print(combined)

# Exercise 10: Count Word Occurrences (Using a Dictionary)
sentence = "the quick brown fox jumps over the lazy dog the fox"
count = {}
for word in sentence.split():
    count[word] = count.get(word, 0) + 1
print(count)

# Exercise 11: Unique Elements in Two Sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
unique = set1.union(set2)
print(unique)

common = set1.intersection(set2)
print(common)

onlyinset1 = set1.difference(set2)
print(onlyinset1)

# Exercise 12: Tuple Unpacking
persona = ("Alice", 25, "Paris")
name, age, city = persona
print(name, age, city)

# Exercise 13: Frequency Counter with Dictionary
text = "hello world"
letter_count = {}
for letter in text:
    if letter != " ":
        letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)

# Exercise 14: Sorting a List of Tuples
students = [("Alice", 90), ("Bob", 80), ("Charlie", 85)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)