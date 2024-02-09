something = 2  # This is a global variable


def hero(number):
    global something  # This is a local variable
    something = number + 4


hero(5)

print("The number iss :: ", something)
