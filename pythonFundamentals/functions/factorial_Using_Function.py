def factorial(n):
    print("This program prints the factorial of ", n)
    result = 1  # addition ma 0 multiplication ma 1
    for i in range(1, n + 1):
        result = result * i
    return result


value = factorial(5)
print("The factorial of a number is ", value)
