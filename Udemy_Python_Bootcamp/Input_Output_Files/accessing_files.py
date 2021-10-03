myfile = open('text.txt') # opening a file and assigning to an object
print(myfile.read()) # read everything in the file. Remember that when we read the file once the cursor goes
# to the end of the file. To reset the cursor to the beginning use myfile.seek(0)
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines()) # returns every line on the file as a list
myfile.close() # always use this after all the operations

# if you do not need to worry about closing the file use
with open('text.txt') as my_new_file :
    content = my_new_file.read()
    print(content)
    my_new_file.seek(0)

#reading and writing mode. Use r to read and w to write and a to append


# appending example
with open('text.txt',mode='a') as new_file_op :
    new_file_op.seek(0)
    new_file_op.write('\n Four on fourth')
    print(new_file_op.read())
# writing example
with open('newfile.txt', mode = 'w') as f_write :
    f_write.write('I created this file')
with open('newfile.txt', mode='r') as f :
    print(f.read())
