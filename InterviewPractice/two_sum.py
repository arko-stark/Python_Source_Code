def two_sum(mylist,num):
    l = len(mylist)
    ret_list=[]
    if(l==0 or l==1):
        return 'Not Possible'
    else :
        for i in range(0,l-1):
            for j in range(i+1,l):
                if (mylist[i]+mylist[j]==num):
                    ret_list.append((mylist[i],mylist[j]))
        return ret_list



l1 = [1,2,3,-2,-1]
n = 0
print(two_sum(l1,n))