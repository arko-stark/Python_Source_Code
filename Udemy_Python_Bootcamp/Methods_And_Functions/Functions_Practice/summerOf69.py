def summer_69(mylist) :
    sum = 0
    add = True
    for num in mylist :
        while add :
            if num != 6 :
                sum = sum+num
                break
            else :
                add = False
        while not add:
            if num != 9 :
                break
            else :
                add = True
                break
    return sum
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))