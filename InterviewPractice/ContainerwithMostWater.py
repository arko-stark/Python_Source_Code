def container(mylist):
    first = 0
    second = 0
    if len(mylist) < 2 :
        return 'Not Possible'
    else :
        first = max(mylist)
        mylist = mylist.pop(mylist.index(first))
        second = max(mylist)
        return (first,second)


test_list = [1,8,6,2,5,4,8,3,7]
# for (a,b) in container(test_list) :
#     print(a)
container(test_list)