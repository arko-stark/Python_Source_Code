def wordcount(mystring, myword) :
    len_word = len(myword)
    mynum = 0
    for i in range(0, len(mystring) - len_word + 1):
        if mystring[i:i + len_word] == myword:
            mynum+=1
            continue
        else:
            pass
    return mynum

print(wordcount("Hellllo","ll"))