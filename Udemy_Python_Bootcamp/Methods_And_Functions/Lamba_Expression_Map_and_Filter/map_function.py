# takes in a function and return square for a list
def square(x) :
    return x**2
mylist = [1,2,3,4,5]

print(list(map(square,mylist)))


# map function on string

def string_len_even(mystring) :
    if len(mystring) % 2== 0 :
        return mystring
    else :
        return mystring[0]
myStringList = ['Andy', 'Biku', 'Johanatha', 'Era']
print(list(map(string_len_even, myStringList)))
