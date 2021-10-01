myname = 'Arko'
print('This is my name : {}'.format(myname))

print('{} is my wife'.format('Bikalpa'))

# .format() by index position
print('The {1} {2} {0}'.format('fox', 'quick','brown'))

#format by variable assignment
print('The name of our kids are {g} and {m}'.format(g='golu',m='molu'))

# float formatting {value:width.precision f}
result = 1000/77
print('The value is {r:1.3f}'.format(r=result))

#f formatting : formatted string literals
name = 'Arko'
wife = 'Bikalpa'
print (f"Hello my name is {name} and my wife's name is {wife}")