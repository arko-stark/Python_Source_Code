msg = 'Hello World'
try :
    astr = int(msg)
except :
    astr = -1
print('this time',astr)

msg = '123'
try :
    astr = int(msg)
except :
    astr = -2
print('this time',astr)
