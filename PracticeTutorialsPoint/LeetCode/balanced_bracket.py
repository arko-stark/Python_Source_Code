def balanced1(str1):
    dict_str = {')':'(','}':'{',']':'['}
    mylist = []
    # if len(str1)== 0 or len(str1) == 1 :
    #     return 'Balanced'
    # else :
    for i in str1 :
        if i in dict_str.values():
            mylist.append(i)
        elif i in dict_str.keys():
            if((mylist[-1] == dict_str[i]) and len(mylist)>0):
                mylist.pop()
                continue
            else :
                return 'Unbalanced'
        else :
            pass
    if len(mylist) == 0:
        return 'Balanced'
    else :
        return 'Unbalanced'

mystring = '{}'
print(balanced1(mystring))
#
#
#
#
# str_1 = ""
# print(is_balanced(str_1))