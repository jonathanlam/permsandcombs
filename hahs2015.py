# Four digit numbers are to be formed from the digits 1, 2, 3 and 4. 
# Each digit is used once only. 
# What is the sum of all the numbers that can be formed?

from itertools import permutations

numbers = [''.join(p) for p in permutations("1234")]

sum = 0
for n in numbers:
    sum += int(n)

print(sum)
# sum = 66660
