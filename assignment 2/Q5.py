my_dict = {
    "name": "<your name>",
    "roll_no": "<your roll number>",
    "branch": "<your branch>",
    "age": 19,
    "city": "<your home city>"
}

print(my_dict)
# i. Rename key "city" to "location"
my_dict["location"] = my_dict.pop("city")

print(my_dict)

# ii. Add a new key "cgpa"
my_dict["cgpa"] = 7.96

print(my_dict)

# iii. Increase age by 1
my_dict["age"] += 1

print(my_dict)

# iv. Delete "branch" using pop()
dict_pop = my_dict.copy()
dict_pop.pop("branch")

print(dict_pop)

# Delete "branch" using del
dict_del = my_dict.copy()
del dict_del["branch"]

print(dict_del)

# pop() returns the removed value, while del only deletes the key.

# v. Iterate using items()
print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(f"{key} → {value}")

# vi. Check whether "email" exists
if "email" in my_dict:
    print("\nEmail:", my_dict["email"])
else:
    print("\nEmail key is not present.")

# vii. Create second dictionary
friend_dict = {
    "name": "Rahul",
    "age": 20,
    "email": "rahul@example.com",
    "college": "ABC College",
    "city": "Patiala"
}

merged_dict = {**my_dict, **friend_dict}

print(merged_dict)

# viii. Dictionary comprehension
# Keep only key-value pairs whose value is a string
string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print(string_values)