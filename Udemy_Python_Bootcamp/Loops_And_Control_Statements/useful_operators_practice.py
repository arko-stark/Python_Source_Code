from random import randint
from random import shuffle

# range function
my_range_list = [1,2,3,4,5,6,7,8,9]
for item in range(0,5,1) : # start at 0 stop at 4 and with step 1
    print(my_range_list[item])
print (list(range(0,9,2))) # returns a list with all the even numbers from 0 to 9


# enumerate function
mysting = "Hello World"
for item in enumerate(mysting):
    print(item) # returns the index position and the items as index
for (a,b) in enumerate(mysting): # tuples unpacking with enumerate
    print(b)


# zip function
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']

for items in zip(mylist2, mylist1):
    print (items) # returns tuples but only till c
for (a,b) in zip(mylist2,mylist1): #tuples unpacking using zip
    print(b)
mydict = {"Name": "Arko", "Age":30}

for dict_items in zip(mydict.values()): #using enumerate on dictionary
    print(dict_items)

# in operator
mylistnum = [1,4,45,34]
print (1 in mylistnum) #returns true
print (2 in mylistnum) #returns false

print("Name" in mydict) #returns true. Dictionary iterate on the key
print(30 in mydict.values()) #returns true. Dictionary iterate on the values



#min, max and rand (mathematical operators)
mylistnum = [1,4,45,34]
print(max(mylistnum)) #returns the maximum number in the list
print(min(mylistnum))

my_random_int = randint(0,100) # random integer generated between 0, 100
print(my_random_int)

# shuffling a list
list_shuf = [1,2,3,4,5,6,7]
shuffle(list_shuf) # inplace function, cannot be used with a print
print(list_shuf)