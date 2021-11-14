try :
    f = open('textfile1', 'w') # change to r to induce an error
    f.write("Hello World")
except TypeError :
    print ('TypeError')
except OSError :
    print('OS Error')
except :
    print('All other error')
finally :
    print('I always run')