def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        arr[left] = key
    return arr

arr1 = [32,1,43,2,3,11,3]
print(binary_insertion_sort(arr1))