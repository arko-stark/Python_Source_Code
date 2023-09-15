def first_occurance(haystack,needle):
    l = len(needle)
    l2 = len(haystack)
    start = 0
    #return haystack[start:l]
    for i in range(0,l2):
        # print(i)
        temp = haystack[i:i+l]
        # print(temp)
        if temp == needle:
            return i
        else :
            continue
    return -1


h = "sadbutsad"
n = "adbu"
print(first_occurance(h,n))