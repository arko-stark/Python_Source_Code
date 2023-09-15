def two_sum(nums,target):
    l = len(nums)
    mylist = []
    for i in range(0,l):
        for j in range(i+1,l):
            if nums[i]+nums[j] == target :
                mylist.append([i,j])
    return mylist

nums = [0,7,2,11,15,5,4]
target = 9

print(two_sum(nums, target))