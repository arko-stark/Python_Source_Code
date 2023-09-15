def two_sum(list1,target) :
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j] == target :
                print(i,j)
                continue


nums = [2,7,11,15]
target = 9
two_sum(nums, target)
