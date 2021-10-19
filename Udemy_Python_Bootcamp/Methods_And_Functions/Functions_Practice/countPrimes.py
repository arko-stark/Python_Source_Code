def count_primes (num) :
    count = 0
    for pointer in range(2,num+1) :
        for divisor in range (2,pointer) :
            if pointer%divisor == 0 :
                break
