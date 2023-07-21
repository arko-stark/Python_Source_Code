def is_palindrome(num) :
    rev = reverse(num)
    if rev == num :
        print("Pali")
    else :
        print("Not Pali")







def reverse(num) :
    rev = 0
    while (num > 0) :
        extr = num %10
        rev = rev*10 + extr
        num = num//10
    return rev

is_palindrome(121)