def squares():
    while True :
        try :
            mynum = int(input('Enter and Integer : '))
        except :
            print('Invalid Integer')
        else:
            return mynum**2
print(squares())