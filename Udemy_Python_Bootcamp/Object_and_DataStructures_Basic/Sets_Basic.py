myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2) # it wont add since it is already in the set
print(myset)
mylist = [1,1,1,1,11,2,3,4,2,2,2]
print(set(mylist)) # casting a list as a set to remove duplicate values

print (set('Mississipi'))