# return allows to assign the function output to a variable
def return_sum(a,b):
    return a+b
sum = return_sum(10,20)
print(sum)



# using print and return together. Python allows that
def return_sum(a,b):
    print(a+b) # this will print a+b
    return a+b
sum = return_sum(10,20)+20 # this will be 50
print(sum)


# check data types before passing inputs to function
# passing strings to a num return method

def add_up(a,b) :
    return a+b

sum = add_up('10','121')
print(sum) # this print 10121. Considers the parameters as string