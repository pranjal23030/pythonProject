# File Handling in python

# Writing a file

# fout = open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\output.txt', 'w')
# print(fout)
#
# line1 = "Hey, Pranjal!! \n"
# fout.write(line1)
# line2 = "How are you. \n"
# fout.write(line2)
# line3 = "Hope everything is well. \n"
# fout.write(line3)
#
# print("Done with writing")
# fout.close()

# Reading a file

fread = open('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\reading.txt', 'r')

for line in fread:
    print(line.rstrip())

fread.close()
