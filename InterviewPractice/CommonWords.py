def common_words(list1):
    l2 =[]
    for n in list1 :
        l2.append("".join(set(n)))
    print(l2)
    mydict = {}
    for i in l2:
        for j in i:
            if (j in mydict.keys()):
                mydict[j]+=1
            else :
                mydict[j]=1
    print(mydict)









strs = ["fflower", "flow", "flight"]
common_words(strs)