# List version
import time
import numpy as np

a=[1,2,3,4,5]*100000

# Numpy version
arr=np.array([1,2,3,4,5]*100000)
start=time.time()
b=arr*2
print("Time Taken for numpy is:",time.time()-start)
