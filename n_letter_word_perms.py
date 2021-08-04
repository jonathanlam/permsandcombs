from itertools import *
def subword_from_word(word, length=None):
    length = len(word) if length is None else length
    a = [''.join(p) for p in permutations(word, length)]
    a = list(set(a))
    return a

print(len(subword_from_word("PARALLEL", 8)))
