# def find_factorial(n):
#     """
#     Computes the factorial of a given number
#
#     Usage examples:
#     >>> find_factorial(5)
#     'The factorial of 5 is 120'
#     >>> find_factorial(4)
#     'The factorial of 4 is 24'
#     """
#
#     total = 1
#     for i in range(1, n + 1):
#         total = total * i
#     output = f"The factorial of {n} is {total}"
#     return output


#####################################################################

num = int(input("Number till: "))


def find_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(total)


find_sum(num)
