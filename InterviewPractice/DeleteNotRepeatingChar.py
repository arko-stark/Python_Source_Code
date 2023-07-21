def del_non_repeating(str1):
    mydict = {}
    newstr=[]
    for s in str1 :
        if s in mydict.keys():
            mydict[s]+=1
        else :
            mydict[s]=1
    #print(mydict)
    for (a,b) in mydict.items() :
        if b!=1:
            newstr.append(a)
        else:
            continue
    print("".join(newstr))



s1 = "Sanjana##"
del_non_repeating(s1)