# Project Euler Problem 16
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

from math import pow

power_of_2 = int(pow(2,15))
power_of_2 = str(power_of_2)
total = 0
for i in range(0, len(power_of_2)):
    total += int(power_of_2[i])

print "The sum of the digits in 2 ** 1000 is: %d" % total
