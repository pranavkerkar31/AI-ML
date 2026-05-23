import numpy as np

data = np.load("MI(1).npz")

for key in data.files:
    print(f"\nKey: {key}")
    print(data[key])