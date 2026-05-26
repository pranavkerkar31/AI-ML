import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_excel(r'Data Engineering/data_quality_practice_dataset.xlsx')
print(df.ndim)
print(df.shape)

cat=df.select_dtypes(include=['string'])
# print(cat)
print(df.describe())
print(df.isnull().sum()) # Completeness metrics
print(df['Department'].unique())

# profile = ProfileReport(df)
# profile.to_file("data_quality_report.html")