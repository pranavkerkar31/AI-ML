import numpy as np
arr=np.array([1,2,3,np.nan,6])
print(arr)
print(np.nan_to_num(arr))

arr=np.array([[1,2,3],[3,4,5]])
print("\nReshape array")
print(arr.reshape(1,6))

print("\nRavel")
print(arr.ravel())
# print(arr)