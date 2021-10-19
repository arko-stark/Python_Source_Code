def almost_there(num):
    if 90 <= num <= 110 :
        return True
    elif 190 <= num <= 210 :
        return True
    else :
        return False

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))