def isAnagram(s,t):
    if len(s) != len(t):
        print('Not an anagram !!!')
    else :
        l1 = list(s).sort()
        l2 = list(t).sort()
        if l1 == l2 :
            print('Is an Anagram')
        else :
            print('Not an anagram')

s = "cnt"
t = "naa"
isAnagram(s,t)

