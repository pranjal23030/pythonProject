number1 = int(input("Number1: "))
number2 = int(input("Number2: "))


def sub(a1, b1):
    mul = a1 * b1
    div = b1 / a1

    return mul, div


n1, n2 = sub(number1, number2)

print("Multiples: ", n1)
print("Division: ", n2)
