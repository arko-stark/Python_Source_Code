def spy_game(mylist) :
    spy = False
    if len(mylist) < 3 :
        return False
    else :
        for i in range(0,len(mylist)-3) :
            if mylist[i]== 0 :
                if mylist[i+1]== 0 and mylist[i+2]== 7 :
                    spy = True
                else :
                    pass
            else :
                continue
        return spy
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print( spy_game([1,7,2,0,4,5,0]))