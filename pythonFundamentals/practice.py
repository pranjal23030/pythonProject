# for i in range (9,0,-1):
#     print(i)

# simple add function


# number1 = int(input("Enter number1: "))
# number2 = int(input("Enter number1: "))
#
#
# def add_things(n1, n2):
#     add = n1 + n2
#     sub = n1 - n2
#
#     return add, sub
#
#
# addition, subtraction = add_things(number1, number2)
#
# print("Addition:", addition)
# print("Subtraction:", subtraction)


# star

# for i in range(0, 3):
#     for j in range(0, 3):
#         print("*", end="")
#     print("\n")


number1 = int(input("Number1: "))
number2 = int(input("Number2: "))


def sub(a1, b1):
    mul = a1 * b1
    div = b1 / a1

    return mul, div


n1, n2 = sub(number1, number2)

print("Multiple: ", n1)
print("Division: ", n2)
