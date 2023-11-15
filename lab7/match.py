def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    print(seq)
    if not pattern:
        return not seq
    elif not seq:
        return False

    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
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

seq = [['titel', [['bil','apakuk'], 'book']], ['år', 2022]]
pattern = [['titel', [['--', '&'], '&']], ['år', '&']]
print(match(seq, pattern))

#def search(match):