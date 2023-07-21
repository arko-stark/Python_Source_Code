def divide2int(dividend, divisor) :
    quotent = 0
    while (dividend >= divisor):
        quotent +=1
        dividend = dividend - divisor
    return quotent

print(divide2int(6,2))