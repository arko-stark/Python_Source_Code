# simple function to say hello to the name you pass

def say_hello(name):
    print("Hello "+name+". How r you")
    print(f'Hello {name}') # printing using f string literal
    print("How r you")

say_hello("Mithi")


# using default value incase arguments are not passed in the function

def def_say_hello(name = '<You need to pass a name>'):
    print(f'Hello {name}')
def_say_hello() # if you miss to pass a parameter it uses the default value
