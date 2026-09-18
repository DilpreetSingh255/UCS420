import numpy as np

Dilpreet = np.linspace(10, 100, 25)

print("Array:")
print(Dilpreet)

print("\nShape:")
print(Dilpreet.shape)

print("\nTotal Elements:")
print(Dilpreet.size)

print("\nData Type:")
print(Dilpreet.dtype)

print("\nTotal Bytes:")
print(Dilpreet.nbytes)

transpose_array = Dilpreet.reshape(25,1)

print("\nTranspose using reshape:")
print(transpose_array)

print("\nCan we use T attribute?")
print("No, T does not affect a 1-D array.")