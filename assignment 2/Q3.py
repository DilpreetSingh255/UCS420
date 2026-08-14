import random
from collections import Counter

roll_no = int(input("Enter roll number: "))

random.seed(roll_no)

# i. Generate 100 random numbers between 100 and 900
numbers = [random.randint(100, 900) for _ in range(100)]

print(numbers)

# ii. Count and print all odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]

print(len(odd_numbers))
print(odd_numbers)

# iii. Count and print all even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print(len(even_numbers))
print(even_numbers)

# iv. Prime numbers using list comprehension
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = [x for x in numbers if is_prime(x)]

print(len(prime_numbers))
print(prime_numbers)

# v. Most frequently occurring number
frequency = Counter(numbers)
most_frequent_number, frequency_count = frequency.most_common(1)[0]
print("\nMost frequently occurring number:", most_frequent_number)
print("It occurs:", frequency_count, "time(s)")