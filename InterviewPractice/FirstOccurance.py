def first_occu(mystring,substr):
    lstr = len(mystring)
    # print(lstr)
    lsubstr = len(substr)
    # print(lsubstr)
    for i in range(0,lstr-lsubstr+1):
        # print(i)
        print(mystring[i:lsubstr])
        # if mystring[i:lsubstr]==substr :
        #     return i
        #     break






haystack = "sadbutsad" # len = 9
needle = "sad" # len = 3 # 9-3+1 = 7
first_occu(haystack,needle)