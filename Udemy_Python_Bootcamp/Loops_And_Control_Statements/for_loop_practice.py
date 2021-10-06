mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist :
    # check for even number
    if (num%2 == 0) :
        print(num)
    else :
        print(f'Odd number {num}')

#printing sum of all numbers in the list
sum_list = 0
for num in mylist :
    sum_list = sum_list+num
print(f'The sum of all the numbers are : {sum_list}')


# using for loop to iterate through strings
mystring = "Hello World"
for myletter in mystring :
    print(myletter)

# using for loop to iterate through a tuple
my_tup = (1,2,3,4)
for item in my_tup :
    print(item)


##  tuple unpacking using for loop
mylist_tup = [(1,2,3),(4,5,6),(7,8,9)]
for (a,b,c) in mylist_tup :
    print(b) # justs prints the second element in each tuple




##  Iterating through a Dictionary
mydict = {'Name': 'Arko', "Age":37, "Profession": 'Engineer'}
for items in mydict :
    print(items) # this would iterate through all the KEYS only
for (key,value) in mydict.items() : #grabs the dictionary items
    print(key) # this iterate through the keys
    print(value) # this iterates through the values
for items in mydict.values() : # this grabs just the values in the dict
    print(items)
