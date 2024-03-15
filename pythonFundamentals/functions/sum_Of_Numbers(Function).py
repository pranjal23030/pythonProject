# def calc_sum(n):
#     result = 0
#     for i in range(1, n + 1):
#         result = result + i
#
#     return result
#
#
# total = calc_sum(5)
# print("The output is: ", total)

number = int(input("Enter the number till you wanna calculate the sum of: "))


def calc_sum(n):
    total = 1
    for i in range(1, n + 1):
        total = total * i
    print(total)


calc_sum(number)
