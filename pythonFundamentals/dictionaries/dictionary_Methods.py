# # Some methods in dictionary
# # Key value pair


birthdays = {
    "ram": ["12-18-1987", "sum_of_Positive_Integers", 12],
    "sita": "7-6-2003",
    "john": "11-5-1992",
    "rita": "5-4-2001"
}


print(type(birthdays))
print()
print(birthdays)
print()

# # Print all names

for name in birthdays.keys():
    print(name)
print()

# # Print all values

for dob in birthdays.values():
    print(dob)
print()

print(birthdays.items())
print(birthdays["ram"][1])
print()

# # Print both name and birthdays together

# for name, dob in birthdays.items():
#     print(name, ":", dob)
# print()

# # add one item
# birthdays["sum_of_Positive_Integers"] = "09-02-2005"
# print(birthdays)
# print()
#
# # clear all items
# # del birthdays
# # birthdays.clear()
#
# # delete one item
# birthdays.pop("ram")
# print(birthdays)
# print()
#
# search in dictionary
user = input("Enter a user: ").lower()

while user not in birthdays:
    print("User not found")
    break

if user in birthdays:
    print(user, ":", birthdays[user])