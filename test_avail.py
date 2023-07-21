def unique(str):
    mylist = list(str)
    myuniquelist = list(set(mylist))
    mydict = {}

    for i in myuniquelist :
        count = 0
        for j in mylist :
            if i==j :
                count+=1

        mydict[i] = count
    return(mydict.items())

print(unique('AvailAa'))


