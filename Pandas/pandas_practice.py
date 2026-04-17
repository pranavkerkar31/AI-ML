import pandas as pd

a=pd.Series([1,2,3,4,5])
print(a)

# Indexing
print("\nIndexing")
print(a[0:2])
print("\nAccepting only the numbers at specific position")
print(a.iloc[[0,1]])

