#assumption is that the array is sorted
def bin_search(arr,num):
    left = 0
    right = len(arr)-1
    while(left <=right):
        mid = (left+right)//2
        if arr[mid] == num :
            return (f'The position where the number is in {mid+1}')
        elif arr[mid] < num :
            left = mid+1
        else :
            right = mid-1
    return ('The number is not there in the array')


arr1 = [2,3,4,5,6,7,8,10]
num1 = 1
print(bin_search(arr1,num1))