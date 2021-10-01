mystring = "Hello World"

# Indexing Strings
print (mystring[0])
print(mystring[1])
print(mystring[-1]) # reverse indexing
print(mystring[-3]) # reverse indexing

# slicing strings
print(mystring[6:])

print(mystring[1:5]) # grab a substring
print(mystring[1:5:1]) # grab a substring ; same as above
print(mystring[1:5:2]) # grab using step size

print(mystring[::-1]) # reversing string using negative step size