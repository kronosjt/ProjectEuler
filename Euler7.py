# Project Euler Problem 7
# 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math
prime_counter = 1  # Counter for prime numbers found incl 2
number = 3  # Starting with 3. 2 skipped

while(prime_counter < 10001):
    divisor = 2
    isprime = True
    while(divisor <= int(math.sqrt(number))):  # We only need to test divisors
                                                # upto sqrt(num)
        if(number%divisor == 0):
            isprime = False 
            break  # If num is divisible by any number then skip rest
        divisor += 1
    if(isprime == True):
        prime_counter+=1
        
    if(prime_counter == 10001):
        print '10001th prime number: ', number
    number+=2
    


