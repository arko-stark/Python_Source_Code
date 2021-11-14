x = 5
y = 0
try :
    z = x/y
except ZeroDivisionError :
    print('Cannot divide by Zero')
except :
    print('Invalid numbers')
else :
    print(z)
finally :
    print('All Done.')