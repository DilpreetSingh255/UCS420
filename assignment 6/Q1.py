import numpy as np

# Sensor readings
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

print("Original Temperatures:")
print(temperature)

# (a) Add 2°C to every reading
corrected_temp = temperature + 2

print("\nTemperatures after adding +2°C:")
print(corrected_temp)

# (b) Convert Celsius to Fahrenheit
fahrenheit = (temperature * 9/5) + 32

print("\nTemperatures in Fahrenheit:")
print(fahrenheit)

# (c) Readings greater than 32°C
greater_than_32 = temperature[temperature > 32]

print("\nReadings greater than 32°C:")
print(greater_than_32)

# (d) Count readings greater than 32°C
count = np.sum(temperature > 32)

print("\nNumber of readings greater than 32°C:")
print(count)

# (e) Explanation
print("\nExplanation:")
print("Vectorization performs operations on the entire array at once without using loops.")
print("Boolean indexing directly filters required elements using conditions.")
print("Both are faster and require less code than iterating through each element manually.")