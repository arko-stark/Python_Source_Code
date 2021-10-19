def animal_crackers(myString) :
    mylist = myString.split()
    if mylist[0][0] == mylist[1][0] :
        return True
    else :
        return False
print(animal_crackers('My  mimbo'))