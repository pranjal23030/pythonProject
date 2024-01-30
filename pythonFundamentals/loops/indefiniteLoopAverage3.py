def main():
    sum = 0.0
    count = 0

    xStr = input ("Enter a number (<Enter> to quit) >> ")
    while xStr != "":  #nothing/empty string not equals जति बेरसम्म इन्टर गर्दैन , तेत्ति बेरसम्म त् चल्नु पर्यो नि त , एडी इन्टर थिचे भनि चल्दैन 
        x = eval(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit)>> ")
    print("\nThe average of the number is", sum/count)

main()
