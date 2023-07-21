def non_zero_pos(list1):
    first = -1
    last = -1
    mylist = []
    for i in list1:
        if i == 0 and first !=-1 and last !=-1 :
            mylist.append([first,last])
            first = -1
            last = -1
        elif i == 0 and first == -1 and last == -1 :
            continue
        elif i!=0 and first == -1 and last == -1:
            first = i
        elif i!=0 and first !=-1:
            last = i
            continue
        else:
            pass
    return mylist




l1 = [0,1,2,0,0,3,0,0,0,1]
print(non_zero_pos(l1))
# expected O/P = [[0,1],[4,5],[8,8]]