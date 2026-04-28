import pandas as pd

a=pd.Series([10,20,30,40,50])
print(a)
a.name='Price'

# Indexing
print("\nIndexing")
print(a[0:2])
print("\nAccepting only the numbers at specific position")
print(a.iloc[[0,1,3]])


fruits=['apple','banana','guava','oranges','grapes']
a.index=fruits
print(a)


# Conditional Indexing

salary={
    'John': 40000,
    'Alice': 50000,
    'Bob': 60000,
    'Chris': 70000,
    'David': 80000,
    'Smith': 20000
}

# now convert this to the Series
series=pd.Series(salary,name='Salary')
print(series)
print(series.loc['John'])

print("\nAnswer will be in the Boolean format")
print(series>40000)

print("\nAnswer will be the salary of the people whose salary is greater than 30000")
print(series[series>30000])