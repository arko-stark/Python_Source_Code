def longest_prefix(mylist):
    res = ""
    for a in zip(*mylist):
        if len(set(a)) == 1 :
            res = res+a[0]
        else:
            return res
        print(a)

strs = ["flower","flow","flight"]
print(longest_prefix(strs))

# strs1 = ["dog","racecar","car"]
# print(longest_prefix(strs1))