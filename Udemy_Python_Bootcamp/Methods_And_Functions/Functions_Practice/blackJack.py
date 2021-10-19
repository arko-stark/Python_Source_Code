def black_jack(x,y,z):
    if x+y+z <= 21 :
        return x+y+z
    else :
        if x==11 or y==11 or z==11 :
            return x+y+z-10
        else :
            return 'BUST'
print(black_jack(5,6,7))
print(black_jack(9,9,9))
print(black_jack(9,9,11))