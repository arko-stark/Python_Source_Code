def rev(myint):
    rev1 = 0
    if myint < 0 :
        temp = abs(myint)
    else :
        temp = myint
    while(temp >0):
        i = temp%10
        rev1 = rev1*10+i
        temp = temp//10
    if myint < 0 :
        return rev1*-1
    else :
        return rev1



print(rev(-1012))