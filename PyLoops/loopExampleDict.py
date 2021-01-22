my_dict1 = {'k1':123, 'k2':[0,1,2],'k3': 'Henry', 'k4':{'insidekey':100}}
for num in my_dict1 :
    print(my_dict1[num])


# using tuple unpacking in dictionaries

for (key, values) in my_dict1.items() :
    # print only the keys
    print(key)

for (key, values) in my_dict1.items() :
    # print only the values
    print(values)
