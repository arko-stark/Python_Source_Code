# immutability of strings
name = "Sam"
#name[0] = 'P' # we camnot replace S with P since Strings are immutable

print(name)

# concatenate a string and change Sam to Pam
last_letters = name[1:]
name = 'P'+last_letters
print(name)

#multiplication of string
print('he'*2)


