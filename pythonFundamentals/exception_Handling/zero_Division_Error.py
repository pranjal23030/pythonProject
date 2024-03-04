num1 = eval(input('Please enter a number: '))
num2 = eval(input('Please enter another number: '))

try:
    result = num1 // num2
    print(result)

except ZeroDivisionError as e:
    print(e)

except Exception:
    print("Trying to divide by zero.")
