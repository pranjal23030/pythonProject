# Write a program which takes dividend and divisor and outputs quotient and remainder

dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))


def quotient_remainder(n1, n2):
    quotient = n2 // n1
    remainder = n2 % n1

    return quotient, remainder


# त्यो जुन dividend ra divisor देको छ , त्यो चाही n1 ra n2 मा आएर बस्छ ,
# अनि त्यो n1 ra n2 मा चाही operation भएपछि , return गर्दिनछ pheri tyahi
# अनि त्यो हटाउनको लागि चाही हामीले ल्याको a ra b ताकी त्यो a ra b चाही अर्को मा प्रिन्ट होस्

# print(quotient_remainder(divisor, dividend))

a, b = quotient_remainder(divisor, dividend)
print("Quotient: ", a)
print("Remainder: ", b)
