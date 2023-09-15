def is_balanced (myBracketString):
    mylist =[]
    mybracket_dict = {']':'[',')':'(','}':'{'}
    # print(mybracket_dict)
    for i in myBracketString :
        if i== '(' or i=='{' or i== '[':
            mylist.append(i)
        elif i== ')' or i=='}' or i== ']':
            if len(mylist) > 0 and mylist[-1]==mybracket_dict[i] :
                mylist.pop()
                continue
            else :
                return False
        else :
            pass
    if len(mylist)== 0 :
        return True
    else :
        return False
mystring = '{}}21'
print(is_balanced(mystring))
