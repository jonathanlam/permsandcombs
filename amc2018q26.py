from itertools import permutations

x = [''.join(p) for p in permutations("ABCDEF")]
answer= []

for item in x:
    if (item.find("A") < item.find("B")) and (item.find("C") < item.find("D")) and (item.find("E") < item.find("F")):
        answer.append(item)

print(len(answer))

# Answer is: 090