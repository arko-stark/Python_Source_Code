str1 = "Hello World"
str = " Arko"

def str_func(str_demo, str2):
    print(str_demo[0])
    print(str_demo[2:5])
    print(str_demo[2:])
    print(str_demo*2)
    print(str_demo+str2)
    print(str2[::-1]) #reverse string

str_func(str1,str)
