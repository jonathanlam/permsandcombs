from itertools import *

# Returns a unique representation of all the rotations and reflections of a particular word
def necklace_lexo(word):
    temp = word + word
    reverse = word[::-1]+word[::-1]
    list1 = [temp[i:i+len(word)] for i in range(len(word))]
    list1.extend([reverse[i:i+len(word)] for i in range(len(word))])
    return min(list1)

def test_necklace_lexo():
    equiv = ["ABC", "BCA", "CAB", "CBA", "BAC", "ACB"]
    for item in equiv:
        assert(lexo(item) == "ABC")
    equiv = ["ABCC", "BCCA", "CCAB", "CABC", "CCAB", "ACCB", "BACC", "CBAC"]
    for item in equiv:
        assert(lexo(item) == "ABCC")
    print("test complete")
    
def necklace_permutations(word):
    # unfortunately this goes through all possible permutations before removing duplicates, so it will run in O(N!) time
    total = {''.join(necklace_lexo(p)) for p in permutations(word)}
    total = list(total)
    return total

# example usage
# How many necklaces made up of 5 red beads and 5 blue beads are there
n = necklace_permutations("AAAAABBBBB")
print(n)
print(len(n))