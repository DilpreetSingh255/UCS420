import numpy as np

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("Steps Matrix:")
print(steps)

# (a) Total steps recorded
total_steps = np.sum(steps)
print("\nTotal Steps Recorded:")
print(total_steps)

# (b) Mean number of steps
mean_steps = np.mean(steps)
print("\nMean Number of Steps:")
print(mean_steps)

# (c) Maximum and Minimum values
max_steps = np.max(steps)
min_steps = np.min(steps)

print("\nMaximum Steps:")
print(max_steps)

print("Minimum Steps:")
print(min_steps)

# (d) Total steps for each day (column-wise)
day_totals = np.sum(steps, axis=0)

print("\nTotal Steps for Each Day:")
print(day_totals)

# (e) Total steps for each user (row-wise)
user_totals = np.sum(steps, axis=1)

print("\nTotal Steps for Each User:")
print(user_totals)

# (f) Position of maximum number of steps
max_position = np.unravel_index(np.argmax(steps), steps.shape)

print("\nPosition of Maximum Steps:")
print(max_position)