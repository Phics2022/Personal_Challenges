#!/usr/bin/python3
# creating a prime number generator
# from a given range of number

import math
print("Input a Number: ", end="")
number=int(input())
nRange=list(map(lambda x:x, range(1, number +1)))
length=int(math.sqrt(number))
parser=[]

print(nRange)
for i in range(length):
    prime = nRange[i]
    for j in nRange:
        if j != prime and j % prime == 0:
            nRange.remove(j)
print(nRange)
