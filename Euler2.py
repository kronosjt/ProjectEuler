# Project Euler.net Problem 2
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms

# first we'll gather all the Fibonacci numbers less tha 4 mil
##fibSequence = (1,2) # tuple to hold the values
##i = 1
##while(i<4000000): # while last element in tuple is <20
##    fibNum = fibSequence[-1] + fibSequence[-2]
##    if(fibNum>=4000000): # if the new number is >20 get out of loop
##        break
##    else:
##        fibSequence = fibSequence + (fibNum,) # else add it to tuple
##    i = int(fibSequence[-1]) # set i to last element in tuple
##print fibSequence
##    
### now check if an element is even, if it is then add to sum
##
##fibSum = 0 
##for x in fibSequence: # walk through the tuple
##    if(x % 2 == 0): # if an element is even the add to sum
##        fibSum = fibSum + x
##print fibSum

# Solution 2
# using a single while loop

# first we'll gather all the Fibonacci numbers less tha 4 mil
##fibSequence = (0,1) # tuple to hold the values
##sum = 0
##while(fibSequence[-1] < 4000000): # while last element in tuple is <4 mil
##    fibNum = fibSequence[-1] + fibSequence[-2]
##    if(fibNum % 2 == 0):
##        sum+=fibNum
##    fibSequence = fibSequence + (fibNum,) # add new num to tuple
##print sum


# Solution 3
# without using a tuple

num1 = 0
num2 = 1
sum = 0
newnum = 0 
while(newnum < 4000000):
    newnum = num1 + num2
    num1 = num2
    num2 = newnum
    if(newnum % 2 == 0):
        sum = sum + newnum
print sum

