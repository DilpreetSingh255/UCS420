roll_no = input("Enter your roll number: ")

L = [int(digit) * 10 for digit in roll_no]

# i. Print L
print(L)

# ii. Add two numbers using append() and insert()
L.append(100)    
print(L)

L.insert(2, 50)    
print(L)

# iii. Remove two elements using remove() and pop()
L.remove(50)      
print(L)

removed = L.pop(1)
print(removed)
print(L)

# iv. Sort ascending and descending
L.sort()
print(L)

L.sort(reverse=True)
print("Descending order:", L)

# v. Slicing
print("First 3 and last 3 elements:", L[:3], L[-3:])

# vi. List comprehension for elements greater than average
average = sum(L) / len(L)

greater_than_average = [x for x in L if x > average]

print("Average of L:", average)
print(greater_than_average)