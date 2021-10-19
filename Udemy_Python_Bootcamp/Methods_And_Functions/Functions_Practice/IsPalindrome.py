def is_palindrome(mystring):
    newString = mystring[::-1]
    print(newString)
    if newString == mystring :
        print('Is a Palindrome')
    else :
        print('Not a Palindrome')
is_palindrome("helleh")