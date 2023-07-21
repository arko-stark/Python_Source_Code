s = "Arko is a murgi"
c1 = list(s) # translating string to character array
print(c1)

c2 = s.split()
print(c2)
c3 = []


def binary_insertion_sort(str):
    arr = list(str)
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
    return ''.join(arr)


for i in range(0,len(c2)):
    temp = binary_insertion_sort(c2[i])
    c3.append(temp)
str1 = ' '.join(c3)
print(str1)


