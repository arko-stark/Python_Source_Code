# check even. Filter function filters the list by the function

def check_even(mynum):
    if mynum % 2 == 0:
        return mynum
    else :
        pass
mylist = [1,2,3,4,5,6]

print(list(filter(check_even,mylist)))