# Some methods in dictionary
# keys value pair


birthdays = {
    "ram": ["12-18-1987", "pranjal", 12],
    "sita": "7-6-2003",
    "john": "11-5-1992",
    "rita": "5-4-2001"
}

print(type(birthdays))
print()
print(birthdays)
print()

# Print all names

for name in birthdays.keys():
    print(name)
print()

# Print all values

for dob in birthdays.values():
    print(dob)
print()

print(birthdays.items())
print(birthdays["ram"][1])
print()

# Print both name and birthdays together

for name, dob in birthdays.items():
    print(name, ":", dob)
print()

# add one item
birthdays["pranjal"] = "09-02-2005"
print(birthdays)
print()
print(birthdays.items())

# clear all items
# del birthdays
# birthdays.clear()

# delete one item
birthdays.pop("ram")
print(birthdays)
print()

# search in dictionary
user = input("Enter a user: ").lower()

if user in birthdays:
    print(user, ":", birthdays[user])
else:
    print("User not found")
