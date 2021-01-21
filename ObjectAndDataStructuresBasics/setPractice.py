my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(2)

# notice in this that the 2 is added just once
print(my_set)

# type casting a list to set to find unique values

my_list = [1,1,1,1,2,2,2,1,1,2, 'Arko', 'Arko']
print(set(my_list))