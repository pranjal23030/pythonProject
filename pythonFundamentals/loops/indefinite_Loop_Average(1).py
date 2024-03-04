def main():
    more_data = 'yes'
    total = 0.0
    count = 0
    while more_data[0] == 'y':
        x = eval(input("Enter a number >> "))
        total = total + x
        count = count + 1
        more_data = input("Do you have more numbers (yes or no) ? ").lower()
    print("\n The average of the numbers is", total / count)


main()
