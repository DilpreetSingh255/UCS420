# i. Create List from your 10-digit roll number
roll_number = input("Enter your roll number: ")
L = [int(digit) * 10 for digit in roll_number]
print("L =", L)

# ii. Add two numbers
L.append(50)
print(L)
L.insert(2, 70)
print(L)

# iii. Remove two elements
L.remove(50)
print(L)
L.pop()
print("After pop():", L)

# iv. Sort
L.sort()
print(L)
L.sort(reverse=True)
print(L)

# v. Slicing
print("First three:", L[:3])
print("Last three:", L[-3:])

# vi. List comprehension

average = sum(L) / len(L)
new_list = [x for x in L if x > average]
print(average)
print(new_list)