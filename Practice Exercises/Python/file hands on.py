# Exercise 1: Reading a JSON File
import json
with open('C:/Users/USER/PycharmProjects/pythonProject/data.json', 'r') as file:
    data = json.load(file)
print(data)

# Exercise 2: Writing to a JSON File
profile = {
    "name": "Jane Smith",
    "age": 28,
    "city": "Los Angeles",
    "hobbies": ["Photography", "Traveling", "Reading"]
}
with open('profile.json', 'w') as file:
    json.dump(profile, file)
print("Profile data saved")

# Exercise 3: Converting CSV to JSON
import csv
import json
students = []
with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)
with open('students.json', 'w') as jsonfile:
    json.dump(students, jsonfile, indent=4)
print("CSV data converted and saved to students.json")

# Exercise 4: Converting JSON to CSV
import json
import csv
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data.keys())
    writer.writerow(data.values())
print("JSON data converted and saved to data.csv")

# Exercise 5: Nested JSON Parsing
import json
with open('books.json', 'r') as file:
    books_data = json.load(file)
for book in books_data['books']:
    print(book['title'])
