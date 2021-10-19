def paper_doll (myString):
    mynewString = ''
    for i in myString :
        mynewString = mynewString+i*3
    return mynewString


myNewString1 = 'Hello'
myNewString2 = 'Mississippi'
print(paper_doll(myNewString1))
print(paper_doll(myNewString2))
