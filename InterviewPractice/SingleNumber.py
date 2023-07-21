def single_num(mylist):
    for i in range(0,len(mylist)-1,1):
        for j in range(i+1, len(mylist),1) :
            if mylist[i]==mylist[j]:
                continue
            else :
                return mylist[i]


nums = [2,2,1]
print(single_num(nums))