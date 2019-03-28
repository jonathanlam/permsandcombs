from itertools import *

def subword_from_word(word, length=None):
    """ Answers a question of the form 'How
    many ways can you form a _length_ letter
    word from _word_
    The function returns a list of these words
    """
    length = len(word) if length is None else length
    a = {''.join(p) for p in permutations(word, length)}
    a = list(a)
    return a

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
    
def necklace_count(word):
    total = {''.join(lexo(p)) for p in permutations(word)}
    total = list(total)
    return total
