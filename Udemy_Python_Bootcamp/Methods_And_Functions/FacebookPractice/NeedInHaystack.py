def search_string (haystack, needle):
    ''''''
    len_needle = len(needle)
    mynum = -1
    for i in range(0,len(haystack)-len_needle+1):
        if haystack[i:i+len_needle] == needle :
            mynum = i
            break
        else :
            continue
    return mynum


haystack = "Hello"
needle = "ll"
print(search_string(haystack,needle))


