def quicksort(arr):
    if len(arr)<=1:
        return arr
    greater = []
    lesser = []
    pivot = arr.pop()
    for item in arr :
        if item > pivot :
            greater.append(item)
        else :
            lesser.append(item)
    return quicksort(lesser)+[pivot]+quicksort(greater)

arr1 = [9,1,4,6,20,11,2]
print(quicksort(arr1))