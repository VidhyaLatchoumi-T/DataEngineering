empty=[]
num=[1,2,3,4,5]
mixed=[1,'Hello',3.14,True]
print(empty)
print(num)
print(mixed)

first=num[0]
third=num[2]
last=num[-1]
print("First element: ",first)
print("Third element: ",third)
print("Last element: ",last)

num[0]=10
num[2]=30
print(num)

num.append(6)
num.insert(2,2.5)
num.extend([23,56,8])
print(num)

num.remove(5) #value
popped= num.pop(2) #index
print(num)

first3=num[:3]
mid3=num[1:4]
last3=num[-3:]
print("First 3 elements: ",first3)
print("Middle 3 elements: ",mid3)
print("Last 3 elements: ",last3)

for n in num:
    print(n)

squares=[x**2 for x in range(6)]
print(squares)