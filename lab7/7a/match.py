# -*- coding: utf-8 -*-
from books import *

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        first = match(seq[0], pattern[0])
        rest = match(seq[1:], pattern[1:])
        return first and rest
    else:
        return False


def search(pattern, db):
    lst = []
    for item in db: 
        if match(item, pattern):
            lst.append(item)
    return lst
 
pattern1 = [['fÃ¶rfattare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['Ã¥r', '&']]

# print(search(pattern1, db))

test_pattern_4 = [['player', ['&', '--']], ['FMVP', ['amount', '&']], ['DPOY', ['amount', '&']], ['chips', ['amount', '&']]]

test_seq_2 = [
[['player', ['Kawhi', 'Leonard']], ['FMVP', ['amount', 2]], ['DPOY', ['amount', 2]], ['chips', ['amount', 2]]],
[['player', ['Giannis', 'Antetokounmpo']], ['MVP', ['amount', 2]], ['FMVP', ['amount', 1]], ['DPOY', ['amount', 2]], ['chips', ['amount', 1]]],
[['player', ['Nikola', 'Jokic']], ['MVP', ['amount', 2]], ['FMVP', ['amount', 1]], ['chips', ['amount', 1]]]

]
"""
def test_final(pattern, db):
        lst = []
        for i,item in db:
            zip(item,)


        
        return lst
"""