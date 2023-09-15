def armstrong(n):
    # return str(n)
    l = int(len(str(n)))
    x = n
    temp = 0
    while(n > 0):
        lst = n%10
        temp = temp+ lst**l
        n = n//10
    if (temp==x):
        return True
    else :
        return False
    # return temp,x

x =123
print(armstrong(x))