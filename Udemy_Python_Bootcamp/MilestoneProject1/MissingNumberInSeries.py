def missing_numer(mylist) :
    l1 = len(mylist)+1
    sum_total = (l1*(1+l1))//2
    sum_list = 0
    for item in mylist :
        sum_list += item
    return sum_total-sum_list

list1 = [2,3,4,7,5,1]
print(missing_numer(list1))