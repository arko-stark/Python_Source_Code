#keys in dict are always string
my_dict={'k1':123,'k2':[0,1,2]}

#get values by passing in the key
a = my_dict['k1']
print(a)

#adding an element
my_dict['k3'] = 24

print(my_dict)


#print the keys
print(my_dict.keys())
#print the values
print(my_dict.values())