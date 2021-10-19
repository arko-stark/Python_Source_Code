def string_rev (mystring):
    mylist = mystring.split()
    mynewlist = mylist[::-1]
    return ' '.join(mynewlist)

print(string_rev("Hello World here I come"))