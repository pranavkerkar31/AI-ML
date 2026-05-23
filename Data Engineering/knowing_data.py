import pandas as pd
import numpy as np
df = pd.read_excel(r'Data Engineering/sample_student_dataset.xlsx')

print(df)
print("\nKnowing the Dimension of the Data...")
print(df.shape)
print(df.ndim)
print(df.columns) # prints the column names
print(df.dtypes) # prints the data types of each column
print(df.size) # row X colounn
# print(df.info())

print("\nSeperating the Numerical and Categorical Data")
print('\nNumerical Data')
coloumns = df.select_dtypes(include=np.number)
print(coloumns)

print('\nCategorical Data')
categorical=df.select_dtypes(include=['object'])
print(categorical)


print('\nChecking the number of missing values')
print(df.isnull().sum())

print('\nStatistics of the Data')
print(df.describe())