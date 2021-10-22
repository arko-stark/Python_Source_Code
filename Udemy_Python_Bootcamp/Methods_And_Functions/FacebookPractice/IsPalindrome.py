def is_palindrome(mynum):
    revnum = 0
    thisnum = mynum
    while thisnum > 0 :
        lastnum = thisnum%10
        revnum = revnum*10 + lastnum
        thisnum = thisnum//10
    return mynum==revnum
print(is_palindrome(-121))