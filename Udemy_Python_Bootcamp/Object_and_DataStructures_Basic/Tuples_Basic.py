my_tuple = (1,2,'Mithi')

print(my_tuple[1]) # indexing in tuple
print(my_tuple[-1]) # reverse indexing in tuple

print(len(my_tuple)) # length of the tuple

print(my_tuple.count(2)) #count of a particular element in the tuple

print(my_tuple.index('Mithi')) # index of a particular element in the tuple

my_tuple[0] = 1 # tuples are immutable so this operation is invalid. Lists support this