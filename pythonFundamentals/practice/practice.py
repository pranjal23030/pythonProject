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

s = "apple orange grapes cat"
l = s.split()
print(l)
print(len(l))

l_new = s.split(",")
print(l_new)
print(len(l_new))
