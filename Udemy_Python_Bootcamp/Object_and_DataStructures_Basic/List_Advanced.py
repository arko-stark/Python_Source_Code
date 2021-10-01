mylist = ["one","two","three"]
print(mylist)
mylist[0] = "ONE" # mutate or change one element in a list
print(mylist)
mylist.append(20.1) # append a new item to end of the list
print(mylist)
popped_item = mylist.pop() #pop off an item from the end of a list
print(popped_item)
print(mylist)

popped_item = mylist.pop(0) # pop at a specific index
print(popped_item)
print(mylist)
popped_item = mylist.pop(-1) # pop on reverse index
print(popped_item)

new_list = ['a','x','z','b']
new_num_list = [1,53,8,100]
new_list.sort() # in place sorting for a list. cannot be assigned to any variable or printed inline
print(new_list)

new_num_list.reverse() # in place reverse sorting for a list. cannot be assigned to any variable or printed inline
print(new_num_list)