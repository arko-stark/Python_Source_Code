def isBalanced(mystring):
    dict = {')':'(','}':'{',']':'['}
    mylist = []
    for i in mystring :
        # print(i)
        if (i=='(' or i=='{' or i=='['):
            mylist.append(i)
        elif (i==')' or i=='}' or i==']'):
            if (len(mylist) > 0 and mylist[-1]==dict[i]) :
                mylist.pop()
                continue
            else :
                return False
        else :
            pass
    if (len(mylist)==0):
        return True
    else :
        return True


print(isBalanced("{}}"))
