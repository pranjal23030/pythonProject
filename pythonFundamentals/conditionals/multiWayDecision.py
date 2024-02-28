def main():
    eutaCharacter = input("Enter any character: ")
    print("You have entered ", eutaCharacter)

    if eutaCharacter[0].isalpha():
        print(eutaCharacter[0] + " is an alphabet")

    elif eutaCharacter[0].isdigit():
        print(eutaCharacter[0] + " is a digit")

    else:
        print(eutaCharacter[0] + " is a special character")


main()
