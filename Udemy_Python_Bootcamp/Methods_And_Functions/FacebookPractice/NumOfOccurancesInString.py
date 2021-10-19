def count_occurances(mystring,mychar) :
    count = 0
    for i in mystring :
        if mychar == i :
            count+=1
        else :
            pass
    return count

print(count_occurances('ARKAPRABHA DUTTA','A'))

print('a'.upper())