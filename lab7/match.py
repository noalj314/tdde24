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
 







seq1 = [ [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
       [['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                  'computer', 'science']],
       ['år', 2010]]  
]

pattern1 = [['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']]

seq2 = [['titel', ['python',], ['år', 2010]]]
seq3 = [[['python']], ['år', '&']]


print(search(pattern1,db))

