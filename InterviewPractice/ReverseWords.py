def rev_words(myString):
    mylist = myString.split()
    return " ".join(mylist[::-1])



strs = "The  123   White     Brown    Fox"
print(rev_words(strs))