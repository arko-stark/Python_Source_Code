def replace_list_item(mylist) :
    l = len(mylist)
    position = -1
    while position<0 or position >l  :
        position = int(input('Enter an index position : '))
    replace_num = int(input('Enter a number to replace with:'))
    mylist[position]=replace_num
    return mylist



def display_list(mylist):
    print(mylist)

newlist = [1,2,3,4,5,6,7,8]

display_list(newlist)
print(replace_list_item(newlist))
