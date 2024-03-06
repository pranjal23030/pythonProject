# Without recursion

# def factorial(n):
#     total = 1
#     for i in range(1, n + 1):
#         total = total * i
#     return total
#
#
# print(factorial(5))

# With recursion

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))


# Sum of Positive Integers
def calc_sum(n):
    total = 0
    if n < 2:
        return n
    else:
        return n + calc_sum(n - 1)


print(calc_sum(5))
