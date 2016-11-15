# Project Euler.net Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000

##sum = 0
##for n in range(1, 1000):
##    if(n % 3 == 0 or n % 5 == 0):
##        sum+=n
##
##print 'Sum of all multiples of 3 or 5 below 1000: ', sum

# Solving using Arithmetic Progression
# If we list down the multiples of 3 & 5 we get:
# 3 5 6 9 10 12 15 18 20 21...
# The difference between the numbers in the sequence follow the pattern:
# 2 1 3 1 2 3 3

sum = 0
newnum = 3
limit = 10000000
while(newnum < limit):
    sum = sum + newnum # latest value of newnum gets added here
    newnum = newnum + 2 # 3+2=5
    if(newnum >= limit): break
    sum = sum + newnum
    newnum = newnum + 1 # 5+1=6
    if(newnum >= limit): break
    sum = sum + newnum
    newnum = newnum + 3 # 6+3=9
    if(newnum >= limit): break
    sum = sum + newnum
    newnum = newnum + 1 # 9+1=10
    if(newnum >= limit): break
    sum = sum + newnum
    newnum = newnum + 2 # 10+2=12
    if(newnum >= limit): break
    sum = sum + newnum
    newnum = newnum + 3 # 12+3=15
    if(newnum >= limit): break
    sum = sum + newnum
    newnum = newnum + 3 # 15+3=18 and so on
    if(newnum >= limit): break

print ('Sum= ', sum)

# just adding some comments for learning Atom
