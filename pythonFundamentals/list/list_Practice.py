numbers = [10, 22, 32, 64, 128, 256, 323]

#################################################
# print(numbers[-1])
# print("List: ", numbers)
# print("Type:", type(numbers))
# print("Length", len(numbers))


#################################################
# List methods
# numbers.append(999)
# print(numbers)

################################################
# Lists are mutable
# print("Before replacing by 100", numbers)
# numbers[2] = 100
# print("After replacing by 100", numbers)

################################################
# strings are immutable

# s = 'apple'
# s[2] = 'x'
# print(s)


################################################
# Empty lists

# l = []
# print(l)
# l.append("Pranjal")
# print(l)
# l.pop()
# print(l)


################################################
# POP METHODS

# print("Before popping out: ", numbers)
# print("POP: ", numbers.pop(0))
# print("After popping out: ", numbers)
# print("POP again: ", numbers.pop())
# print(numbers)
# print("POP ONCE AGAIN: ", numbers.pop(2))
# print(numbers)

########################################################################
# LIST ADDITION AND REMOVE

# print(numbers)
# numbers.insert(2, 100)
# print("INSERT at 2: ",  numbers)
#
# print("Before removing: ", numbers)
# numbers.remove(100)
# print("After removing: ", numbers)

########################################################################
# List addition

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# list3 = list1 + list2
# print("LIST3 : ", list3)

# List append
# print("List1 before append: ", list1)
# list1.append(list2)
# print("List1 after append: ", list1)
# print(list1[0])
# print(list1[3])
#
# print(list1[3][1])
#
# ####################################################
# l = [1, 7, 9, [5, 2, [3, 8]], 6, 0]
# print(l[3][2][1])

#########################################################
# List and string

# s = "apple"
# print(type(s))
#
# l = list(s)
# print(type(l))
#
# print("S is: ", s)
# print("L is: ", l)
# print("Splitted list: ", s.split())

#############################################
# String lists split

# s = "blowing-in the wind"
# l = list(s)
# print(l)
#
# l = s.split()  # je bhettincha tyai bata kattincha by default space hercha
# print(l)
# print(len(l))

######################################################################
l = ["rato", "tika", "nidhar", "ma"]
print(l)
print("L is of type: ", type(l))

s = " ".join(l)
print(s)
print("s is of type: ", type(s))
