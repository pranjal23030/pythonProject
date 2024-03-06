# def countdown(n):
#     if n <= 0:
#         print("Blastoff")
#     else:
#         print(n)
#         countdown(n - 1)
#
#         #ulto ghumirako cha
#
# countdown(5)

def countdown(n):
    if n <= 0:
        print("Blastoff")
    else:
        countdown(n - 1)
        print(n)


countdown(5)
