# Project Euler.net Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# First find all the factors of n
import math
num = 600851475143
factors = () # tuple to store the factors
factor = 3 # Discarding 2 since we know it is the only even prime

if(num % 2 == 0):
    factors += (2,)

while(factor < int(math.sqrt(num))): # largest fact will be <sqrt of num
    if(num % factor == 0):
        factors += (factor,)
    factor+=2 # only need to check odd numbers
        

# check factors for prime
n = factors[1] # the second element is the largest factor
print factors
##for i in factors:
##    if(i % 2 == 0):
##        print 'not a prime'
