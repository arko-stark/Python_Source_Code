num1 = 10

def ask_for_input():
    while True :
        try :
            num2 = int(input('Enter the Second Number :'))
        except :
            print('Not a valid number')
            continue
        else :
            return num2
            break
        finally :
            print('I will always run no matter what')

print(num1+ask_for_input())