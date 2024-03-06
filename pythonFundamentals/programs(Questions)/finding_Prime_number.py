def is_prime(num):
    if num == 1 or num == 2:
        return True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


for i in range(1, 10):
    if is_prime(i):
        print(i, end=" ")
