def non_duplicate_finder(mylist) :
    templist = []
    for item in mylist :
        if item not in templist :
            templist.append(item)
        else :
            templist.remove(item)
    return templist.pop()

mylist1 = [1,3,1,3,-1]
print(non_duplicate_finder(mylist1))