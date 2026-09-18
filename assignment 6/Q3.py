import numpy as np

# (a) Create array
original = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(original)

# (b) Slice from index 1 to 4
subset = original[1:5]

print("\nSubset:")
print(subset)

# (c) Modify first element of subset
subset[0] = 999

print("\nAfter modifying subset:")
print("Original Array:", original)
print("Subset:", subset)

# (d) Create copy and modify
copied = original.copy()

copied[0] = 500

print("\nAfter modifying copied array:")
print("Original Array:", original)
print("Copied Array:", copied)

# (e) Create 1 to 12 and reshape to 3x4
matrix = np.arange(1, 13).reshape(3, 4)

print("\n3 x 4 Matrix:")
print(matrix)

# (f) Extract elements

print("\nFirst Row:")
print(matrix[0])

print("\nLast Row:")
print(matrix[-1])

print("\nSecond Column:")
print(matrix[:, 1])

print("\nRows 1-2 and Columns 2-3:")
print(matrix[0:2, 1:3])

# (g) Flatten and Ravel

flat_arr = matrix.flatten()
ravel_arr = matrix.ravel()

print("\nFlatten Array:")
print(flat_arr)

print("\nRavel Array:")
print(ravel_arr)

# (h) Modify ravel array
ravel_arr[0] = 100

print("\nAfter modifying ravel:")
print("Original Matrix:")
print(matrix)

# (i) Modify flatten array
flat_arr[1] = 200

print("\nAfter modifying flatten:")
print("Flatten Array:")
print(flat_arr)

print("\nOriginal Matrix:")
print(matrix)

# (j) Shape, ndim, size, dtype

print("\nShape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)