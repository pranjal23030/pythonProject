num1 = eval(input('Please enter a number: '))
num2 = eval(input('Please enter another number: '))
##result = num1/num2
##print(result)

try:
    result = num1/num2
    print(result)

except FileNotFoundError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

except Exception:
    print("Trying to divide by zero.")

    


    
