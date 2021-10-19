def has_33(mylist):
    if len(mylist)<= 1 :
        return False
    else :
        if mylist[0]==3 :
            if mylist[1]==3 :
                return True
        else :
            for i in range(1,len(mylist)-1):
                if mylist[i]==3 :
                    if mylist[i-1]==3 or mylist[i+1]==3 :
                        return True
                    else :
                        pass
                else :
                    pass

print(has_33([3]))
