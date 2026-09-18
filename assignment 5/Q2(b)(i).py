import numpy as np

x = np.array([1,2,3,4,5,1,2,1,1,1])

unique, counts = np.unique(x, return_counts=True)

max_freq_value = unique[np.argmax(counts)]

indices = np.where(x == max_freq_value)

print("Array:")
print(x)

print("Most Frequent Value:", max_freq_value)
print("Indices:", indices[0])