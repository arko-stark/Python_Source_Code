def makes_twenty(x,y):
    if x+y == 20 :
        return True
    elif x==20 or y==20 :
        return True
    else :
        return False

print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(8,12))