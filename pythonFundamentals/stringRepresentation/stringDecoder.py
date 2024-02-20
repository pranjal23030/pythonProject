print('This program converts a unicode number sequence message into')
print('the text that it represents')
stringed_message = input("Enter the text:  ")
message = ""

for num_str in stringed_message.split():
    code_num = int(num_str)
    message = message + chr(code_num)
print("\nThe decoded message is: ", message)
