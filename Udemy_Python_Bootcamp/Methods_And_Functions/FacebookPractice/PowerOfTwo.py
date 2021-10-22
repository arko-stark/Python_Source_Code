def two_power(mynum) :
    if mynum == 1 :
        return True
    else :
        while mynum > 1 :
            if mynum %2 == 0 :
                mynum = mynum/2
            else :
                return False
        return mynum==1

print(two_power(1))