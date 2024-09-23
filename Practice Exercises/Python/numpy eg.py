import numpy as np
arr=np.array([1,2,3,4,5])
print("Array:",arr)

reshaped=np.arange(6).reshape(2,3)
print("reshaped:\n",reshaped)

arr_add=arr+10
print("Added 10: ",arr_add)

arr_mul=arr*2
print("Multiply 2: ",arr_mul)

sliced=arr[1:4]
print("Sliced arr: ",sliced)

