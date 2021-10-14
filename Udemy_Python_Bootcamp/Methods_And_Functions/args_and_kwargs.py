# *args example. *args is used to define arbitrary number of arguments in a function parameters. Returns tuple
def func_args(*args):
    print (sum(args))
func_args(10,40,70,10)



# **kwargs is used for keyword arguments. **returns back a keyword argument. Returns Dictionary
def func_kwargs(**kwargs):
    if 'fruit' in kwargs :
        print('I love {} fruit'.format(kwargs['fruit']))
    else :
        print ('fruit is not present')
func_kwargs(fruit='orange', food = 'egg')




# usings *args and **kwargs in combination
def func_args_kwargs(*args, **kwargs):
    print (sum(args)*20)
    print (kwargs['size'])
func_args_kwargs(10,20,1,2,size = 'M')