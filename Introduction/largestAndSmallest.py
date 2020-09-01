largest = None
smallest = None
while True :
    num = input('Enter a Number :')
    if num == 'done' :
        break
    try :
        num_conv = int (num)
        if smallest is None :
            smallest = num_conv
        if largest is None :
            largest = num_conv
        if num_conv < smallest :
            smallest = num_conv
            continue
        if num_conv > largest :
            largest = num_conv
            continue

    except :
        print('Invalid input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)
