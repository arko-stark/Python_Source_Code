def rev_int(myint):
    r = 0
    while(myint > 0):
        temp = myint%10
        r = r*10+temp
        myint = myint//10
    return r

print(rev_int(1213))