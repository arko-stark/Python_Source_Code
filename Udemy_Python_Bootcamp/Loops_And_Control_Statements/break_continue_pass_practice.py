# pass example
x = 0
mylist = [1,2,3,4,5,6]
for item in mylist :
    pass # this is used as a placeholder. Without pass an empty loop will be an error

# continue example
while (x < 6) :
    x = x+1
    if (x%2 == 0) :
        continue
    print(f'The odd numbers are {x}')

# break example
mystring = "Sammy"
for char in mystring :
    if char == 'm' :
        break
    print(char)