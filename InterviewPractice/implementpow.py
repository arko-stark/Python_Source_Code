def pow_implement(x,y):
    temp =1
    for i in range (0,y):
        temp = temp*x
    return temp

print(pow_implement(2,3))