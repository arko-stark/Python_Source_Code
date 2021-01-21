my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)

# lookup value
print(my_dict['key1'])


# dictionary can hold any data type
my_dict1 = {'k1':123, 'k2':[0,1,2],'k3': 'Henry', 'k4':{'insidekey':100}}
print(my_dict1['k1'])
print(my_dict1['k2'])
print(my_dict1['k3'])
print(my_dict1['k4'])
print(my_dict1['k4']['insidekey'])


# converting to uppercase in a list dictionary
d = {'key1':['a','b','c']}
print(d['key1'][2].upper())

# Adding a new Key Value paid to a dictionary
d['key2'] = 200

print(d)

# override an existing value
d['key2'] = 'Stark'

print(d)

# view all keys in the dictionary
print (d.keys())

# view all values  in the dictionary
print (d.values())

# view all items  in the dictionary as tuples
print (d.items())