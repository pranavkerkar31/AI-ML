# What is Noisy Data?

# Noisy data means data that contains:

# Errors
# Outliers
# Random variations
# Incorrect values

# 1) Clustering
from sklearn.cluster import KMeans
import pandas as pd

df = pd.DataFrame({
    "Age":[22,24,25,27,28,30,26,24,23,60],
    "Salary":[25,28,30,32,35,36,31,29,27,150]
})

kmeans = KMeans(n_clusters=1)
kmeans.fit(df)

print(kmeans.cluster_centers_)
