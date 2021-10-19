def rolling_addition(mylist) :
    mynewlist = []
    if len(mylist) == 0 :
        return mylist
    else :
        mynewlist.append(mylist[0])
        for i in range(1,len(mylist)) :
            newnum = mynewlist[-1]+mylist[i]
            mynewlist.append(newnum)
    print (mynewlist)

rolling_addition([1,2,3,4])