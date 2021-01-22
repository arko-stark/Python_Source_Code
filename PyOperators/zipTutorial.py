# zip only goes as far as the shortest list

list1 =[1,2,3]
list2 = ['a','b','c']
list3 = ['x','y','z']

for item in zip(list1,list2,list3):
    print (item)

# use tuple unpacking on list
for (a,b,c) in zip(list1,list2,list3):
    print (a)