# lambda expression : anonymous function
# creating square function
sqr = lambda num : num**2
print (sqr(5))

# using lambda with map
mylist = [1,2,3,4,5]
print(list(map(lambda num:num**2,mylist)))

# using lambda with filter
myNewlist = [1,2,3,4,5]
print(list(filter(lambda num:num%2==0,mylist)))


#use lambda to grab first character of a string
mynames = ['Andy', 'Sully']
print(list(map(lambda names : names[0], mynames)))