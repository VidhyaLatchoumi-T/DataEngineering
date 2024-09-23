students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "C"},
    {"name": "David", "age": 23, "grade": "B"},
]

print(students[0]["name"])

new_student = {"name": "Eva", "age": 19, "grade": "A"}
students.append(new_student)

for student in students:
    print(f"Name: {student['name']}, "
          f"Age: {student['age']}, "
          f"Grade: {student['grade']}")

