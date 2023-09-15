def add_digits(num1):
    digits = 0
    while(num1 > 0):
        digits = digits+num1%10
        num1 = num1//10
        if num1 == 0 and digits > 9 :
            num1 = digits
            digits = 0
    return digits

nums = 381
print(add_digits(nums))