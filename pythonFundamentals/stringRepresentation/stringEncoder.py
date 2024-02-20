print('This program converts a textual message into a sequence')
print('of numbers representing the Unicode encoding' + \
      'of the message.\n')
message = input("Enter the text:  ")

print('\n Here are the Unicode codes: ')

for ch in message:
    print(ord(ch), end=" ")
print()  # blank line before prompt
