def computepay(h,r):
    if h > 40 :
        pay = (h-40)*1.5*r+40*r
    elif h <= 40 :
        pay = h*r
    else :
        pay = 0
    return pay

hrs = input("Enter Hrs Worked: ")
rate = input("Enter Rate of work in $:")
try :
    hours = float(hrs)
    rt = float(rate)
except :
    print('Please enter hours and rate in correct numeric form only')
p = computepay(hours,rt)
print("Pay",p)
