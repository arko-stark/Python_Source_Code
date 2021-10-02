my_dict = {'Name':'Arko','Age': 30}
print(my_dict['Name']) # get values by passing in the Key
# dictionary can hold lists or even other dictionaries
d = {'k1':123,'k2':[0,1,2]}
print(d['k2'][1])

d['k3'] = 300 # add another KV pair to a dictionary
print(d)

d['k1'] = 'Son' #override value in a dictionary
print(d)
print(d.keys()) # returns all the dictionary keys
print(d.values()) # returns all the dictionary values
print(d.items()) # returns dictionary as tuples