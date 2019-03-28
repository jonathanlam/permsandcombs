from itertools import *

def subword_from_word(word, length=None):
    """ Answers a question of the form 'How
    many ways can you form a _length_ letter
    word from _word_
    The function returns a list of these words
    """
    length = len(word) if length is None else length
    a = [''.join(p) for p in permutations(word, length)]
    a = list(set(a))
    return a
