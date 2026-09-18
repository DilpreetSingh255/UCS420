import numpy as np

ucs420_Dilpreet = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,15,20,35]
])

print("Original Array:")
print(ucs420_Dilpreet)

print("\nMean:")
print(np.mean(ucs420_Dilpreet))

print("\nMedian:")
print(np.median(ucs420_Dilpreet))

print("\nMaximum:")
print(np.max(ucs420_Dilpreet))

print("\nMinimum:")
print(np.min(ucs420_Dilpreet))

print("\nUnique Elements:")
print(np.unique(ucs420_Dilpreet))

reshaped_ucs420_Dilpreet = ucs420_Dilpreet.reshape(4,3)

print("\nReshaped Array (4x3):")
print(reshaped_ucs420_Dilpreet)

resized_ucs420_Dilpreet = np.resize(ucs420_Dilpreet, (2,3))

print("\nResized Array (2x3):")
print(resized_ucs420_Dilpreet)