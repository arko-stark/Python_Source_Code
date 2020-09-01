hrs = input('Enter Hours Worked :')
rate = input('Enter Rate per Hour :')
excess = float(hrs) -  40
if (excess > 0) :
    pay = 40 * float(rate) + excess*float(rate)*1.5
else :
    pay = float(hrs)*float(rate)
print(pay)
