import numpy as np

arr=np.array(np.random.randint(10,50, size=(2)))
print(arr)

# arr=np.array([1,2,3],dtype=np.int16)
# print(arr)

arr=np.random.uniform(10,20,size=(3,4))
print(arr)

print("\nType Conversion")
arr=np.array([1,2,3,4])
print(arr.dtype)
newarr=arr.astype(np.float64)
print(newarr.dtype)