mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist :
    # print (f'the number is {num}')
    if(num%2 == 0) :
        print(f'the even number is {num}')
        list_sum = list_sum + num
print(f'the sum of all the even numbers are {list_sum}')
