def first_and_last(mylist, target):
    output = [-1,-1]
    for i in range(0,len(mylist)) :
        if mylist[i]==target :
            output[0]=i
            break
        # print(i)
    for j in range(len(mylist)-1,0,-1) :
        if mylist[j]==target :
            output[1]=j
            break
    return output
nums = []
tar1 = 0
print(first_and_last(nums,tar1))
first_and_last(nums,tar1)