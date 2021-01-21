myfile = open('test.txt', mode = 'r+')
print(myfile.read())

# SETTING THE CURSOR BACK TO THE BEGINNING OF THE FILE
myfile.seek(0)
print(myfile.read())


# reading every line individually and creating a list out of the lines
myfile.seek(0)
line_list = myfile.readlines()
print(line_list[1])


# writing to a file
myfile.write('\nThis is line 5')
print(myfile.read())

# remember to close a file at the end of the file manipulation
myfile.close()



