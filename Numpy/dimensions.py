import numpy as np

print("\n1D Array")
arr=np.array([1,2,3,4])
print(arr.shape)
print(arr.ndim)

print("------------------------")
print("\n2D Array")
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)

print("------------------------")
print("\n3D Array")
arr=np.array([
    [[1,2,3],
     [4,5,6]],

     [[7,8,9],[10,11,12]]
])
print(arr.shape)
print(arr.ndim)