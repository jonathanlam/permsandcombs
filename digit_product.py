'''
How many positive integers less than 10000 are there
such that its digit-product is 210?
For example 7352 because 7*3*5*2 = 210
'''

def digitProd(i):
    i = str(i)
    count = 1
    for ch in i:
        count *= int(ch)
    return count

count = 0
for i in range(10001):
    if digitProd(i) == 210:
        count += 1
        
print(count)
