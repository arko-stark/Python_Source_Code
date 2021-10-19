def century_finder(year):
    if year%100 == 0 :
        return int(year/100)
    else :
        return year//100+1
century = century_finder(19475)
print(f'You are in the {century}th century')