# How many permutations of the string "AABBCC" are there such that no two adjacent letters are the same?

from itertools import permutations

start = "AABBCC"
dic = set()

for i in permutations(start):
    perm = "".join(i)
    if "AA" in perm or "BB" in perm or "CC" in perm:
        continue
    dic.add(perm)
print(', ' .join(dic))
print(len(dic))
