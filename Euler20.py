# Project Euler Problem 20
# the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of the digits in the number 100!
# I've made this a generic solution for any given number

number = int(raw_input("Enter a number to find factorial for: "))
factorial = 1
for a in range(1, number+1):
    factorial = factorial * a

print "Factorial of %d is: %d" % (number, factorial)

sum_of_digits = 0
factorial = str(factorial)
for i in range(0, len(factorial)):
    sum_of_digits += int(factorial[i])
print "The sum of the digits in %d factorial is: %d" % (number, sum_of_digits)
