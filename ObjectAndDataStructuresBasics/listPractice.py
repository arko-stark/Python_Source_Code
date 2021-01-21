my_list1 = [1,2,3]
print(my_list1)
my_list = ['Arko',1, 2.3]
print(my_list)
print(len(my_list))

# indexing example
print(my_list[2])

# slicing
print(my_list[::-1])

# concatenate
my_list4 = my_list1 + my_list
print(my_list4)
my_list4[0] = 'Stark'
print(my_list4)

# adding to the end of the list
my_list4.append(3)
print(my_list4)

# pop
last_item = my_list4.pop()
print(my_list4)
print(last_item)

#pop again
last_item = my_list4.pop()
print(my_list4)
print(last_item)


# pop at a specific index
spec_item = my_list4.pop(0)
print(my_list4)
print(spec_item)

# sort method
new_list1 = ['a', 'e', 'x','b', 'c']
num_list = [2,1,0, -1, 100, 2]
num_list.sort()
new_list1.sort()
print(num_list)
print(new_list1)

num_list.reverse()
print(num_list)