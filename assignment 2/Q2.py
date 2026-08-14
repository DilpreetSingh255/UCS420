roll_no = input("Enter roll number: ")

L = [int(digit) * 10 for digit in roll_no]

scores = tuple(L[:8])
print(scores)

# i. Highest score and its index
highest = max(scores)
highest_index = scores.index(highest)

# Lowest score and number of times it appears
lowest = min(scores)
lowest_count = scores.count(lowest)

print(highest)
print(highest_index)

print(lowest)
print(lowest_count)

# ii. Reverse tuple and return result as a list
reversed_scores = list(scores[::-1])

print(reversed_scores)

# iii. Ask user for a score
search_score = int(input("Enter a score to search: "))

if search_score in scores:
    print(scores.index(search_score))
else:
    print("Score not present")

# iv. Attempt to change tuple element
try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable, so their elements cannot be changed directly.")

# v. Unpacking using *
first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)