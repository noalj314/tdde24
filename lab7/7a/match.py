# Encoding: ISO-8859-1

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
    """Searches through a database and returns all the items in the db corresponding to the pattern"""
    lst = []
    for item in db: 
        if match(item, pattern):
            lst.append(item)
    return lst
 
