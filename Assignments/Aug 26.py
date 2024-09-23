#Exercise 1: Create a List
fruits=["apple","banana","cherry","date","elderberry"]
print(fruits)

#Exercise 2: Access List Elements
firstelement=fruits[0]
lastelement=fruits[-1]
secondelement=fruits[1]
fourthelement=fruits[3]
print("first element: ",firstelement)
print("last element: ",lastelement)
print("second element: ",secondelement)
print("fourth element: ",fourthelement)

#Exercise 3: Modify a List
fruits[1]="blueberry"
print(fruits)

#Exercise 4: Add and Remove Elements
fruits.extend(["fig","grape"])
fruits.remove("apple")
print(fruits)

#Exercise 5: Slice a List
first_three_fruits=fruits[:3]
print(first_three_fruits)

#Exercise 6: Find List Length
length=len(fruits)
print(length)

#Exercise 7: List Concatenation
vegetables=["carrot","brocolli","spinach"]
food=fruits+vegetables
print(food)

#Exercise 8: Loop Through a List
for f in fruits:
    print (f)

#Exercise 9: Check for Membership
if "cherry" in fruits:
    print("Cherry is present")
else:
    print("Cherry is not present")
if "mango" in fruits:
    print("mango is present")
else:
    print("mango is not present")

#Exercise 10: List Comprehension
fruit_length=[len(f) for f in fruits]
print(fruit_length)

#Exercise 11: Sort a List
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

#Exercise 12: Nested Lists
nested_list=[fruits[:3],fruits[-3:]]
print(nested_list[1][0])

#Exercise 13: Remove Duplicates
numbers=[1,2,2,3,4,4,4,5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

#Exercise 14: Split and Join Strings
words="hello, world, python, programming"
spl=words.split(", ")
final_string=" ".join(spl)
print(final_string)