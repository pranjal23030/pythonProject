word = input("Enter a word: ").lower()

d = {}

for ch in word:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] = d[ch] + 1

print(d)

