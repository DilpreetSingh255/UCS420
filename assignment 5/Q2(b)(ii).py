import numpy as np

y = np.array([1,1,1,2,3,4,2,4,3,3])

unique, counts = np.unique(y, return_counts=True)

max_freq_value = unique[np.argmax(counts)]

indices = np.where(y == max_freq_value)

print("Array:")
print(y)

print("Most Frequent Value:", max_freq_value)
print("Indices:", indices[0])