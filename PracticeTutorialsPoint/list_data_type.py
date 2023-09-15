list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
list_num = [2,1,5,2,4,7,3]
#length of a list
print(len(list))
#Sorting list
list_num.sort()
print(list_num)
#indexing in a list
print(list[0])
# Slicing in a list
print(list[1:3])
#concatenation
print(list+tinylist)
# Mutate/change an element in a list
list[1] = 34
print(list)
# append a new item to the end of the list
list.append(1)
print(list)
# Pop an item from end of a list
temp = list.pop()
print(temp)
print(list)
# pop specific item
temp_2 = list.pop(1)
print(temp_2)
print(list)
# in place sorting
#reverse sorting
list_num.reverse()
print(list_num)
