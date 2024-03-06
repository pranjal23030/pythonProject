# s = "apple"
#
# reversed_s = s[::-1]
#
# print(reversed_s)


# s = 'apple'
# 
# reverse_str = ""
# for i in range(len(s) - 1, -1, -1):
#     reverse_str = reverse_str + s[i]
# 
# print(reverse_str)


s = "apple"

reverse_str = ""
for i in s:
    reverse_str = i + reverse_str

print(reverse_str)
