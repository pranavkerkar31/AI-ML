import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])
print("\nConcatenation")
join=np.concatenate((a,b))
print(join)

print("\nVStack")
vstack=np.vstack((a,b))
print(vstack)

print("\nHStack")
hstack=np.hstack((a,b))
print(hstack)