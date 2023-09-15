def search_insert(nums,target):
    for i in range(0,len(nums)-1):
        if(nums[i]==target):
            return i
        else :
            first = nums[i]
            second = nums[i+1]
            if(target > first and target < second):
                return i+1
            else :
                continue