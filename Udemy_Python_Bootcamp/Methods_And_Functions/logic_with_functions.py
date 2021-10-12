# check whether any number is even inside a list

def check_even_list(numlist):
    for i in numlist:
        if i%2 == 0:
            return True
            break
        else:
            pass
    return False
print(check_even_list([1,3,1]))


# return all the even numbers in a list
def even_list(numlist):
    num_even = []
    for i in numlist:
        if i%2 == 0:
            num_even.append(i)
        else:
            pass
    return num_even
print(even_list([1,3,1]))