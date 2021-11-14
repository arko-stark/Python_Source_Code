def num_count(num, digit):
    count = 0
    for item in range(0,num+1):
        while item > 0 :
            placeval = item%10
            if placeval == digit :
                count+=1
            else :
                pass
            item = item//10
    return count

print(num_count(12,0))
