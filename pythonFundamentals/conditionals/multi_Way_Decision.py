def main():
    character = input("Enter any character: ")
    print("You have entered ", character)

    if character[0].isalpha():
        print(character[0] + " is an alphabet.")

    elif character[0].isdigit():
        print(character[0] + " is a digit.")

    else:
        print(character[0] + " is a special character.")


main()
