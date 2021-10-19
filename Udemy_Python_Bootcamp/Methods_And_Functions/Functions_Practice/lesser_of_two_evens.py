def lesser_even(x,y) :
    if x%2==0 and y%2==0:
        return min(x,y)
    else :
        return max(x,y)

num = lesser_even(101,100)
print(num)