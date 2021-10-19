def rev_num(num):
    reverse_num = 0
    while num > 0 :
        lastnum = num%10
        reverse_num = reverse_num*10 + lastnum
        num = num//10
    return reverse_num

print(rev_num(3000))
print(rev_num(121))
print(rev_num(1231))
print(rev_num(-1231))
print(rev_num(0))
# print (int(7/2))