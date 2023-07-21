def search_inset(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return left

nums = [1,3,5,6]
target = 2
print(search_inset(nums,target))
