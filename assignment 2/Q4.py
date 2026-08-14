roll_no = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_no]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print(A)
print(B)

# vii. Union of A and B
union = A.union(B)
print(union)
# viii. Intersection of A and B
intersection = A.intersection(B)
print(intersection)

# ix. Difference
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print(A_minus_B)
print(B_minus_A)

# x. Symmetric difference
symmetric_diff = A.symmetric_difference(B)

print(symmetric_diff)

# xi. Check subset and superset
print(A.issubset(B))
print(B.issuperset(A))

# Ask user for a value
x = int(input("\nEnter a value to remove from A: "))

A.discard(x)
print("Set A after discard:", A)

# discard() is safer when you are not sure whether the value exists,
# because it does not raise an error if the value is absent.