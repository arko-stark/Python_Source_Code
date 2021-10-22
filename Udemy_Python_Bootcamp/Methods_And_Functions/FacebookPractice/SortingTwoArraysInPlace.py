
# function for inplace sorting or merge sorting
def insert_val(arr,val):
    i = 0
    for item in arr :
        if val > item :
            i+=1
        else :
            arr.insert(i,val)
            return
    arr.insert(i,val)





myvalarr = []
arr1 = [1, 2, 132, 1, 434, 13]
arr2 = [2, 1, -90, 0]
myarr = arr1+arr2
for item in myarr :
    insert_val(myvalarr,item)
print(myvalarr)