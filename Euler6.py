# Project Euler Problem 6
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# sum of squares = n*(n +1)*(2*n +1) /12
# square of sums = (n*(n+1)/2)^2

limit = 100
sumofsquares = 0
for i in range(1, limit + 1):
    sumofsquares = sumofsquares + i*i

print 'Sum of squares of first', limit, ' numbers: ', sumofsquares
    
squareofsums = 0
sumofnums = limit * (limit + 1)/2 #sum of first n nums=n*(n+1)/2
squareofsums = sumofnums * sumofnums
print 'Square of sum of first', limit, ' numbers: ', squareofsums

diff = squareofsums - sumofsquares
print diff
