def int_reverse(myint) :
    rev_int = 0
    new_myint = abs(myint)
    while (new_myint > 0):
        newnum  = new_myint%10
        rev_int = rev_int*10+newnum
        new_myint = new_myint//10
    if myint < 0 :
        return rev_int*-1
    else :
        return rev_int

new_int = -123
print(int_reverse(new_int))