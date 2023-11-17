#from books import *
db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                  'computer', 'science']],
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using',
                  'python', 'and', 'c++']],
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif not seq and pattern != ['--']:
        return False

    if pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif pattern[0] == '--':
        return match(seq, pattern[1:]) or (seq and match(seq[1:], pattern))
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False

    

def search(pattern, db):
    matched_books = []
    for book in db:
        if match(book, pattern):
            matched_books.append(book)
    return matched_books


print(search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db))

print(search(['--', ['år', 2042], '--'], db))

print(search(['--', ['titel', ['&', '&']], '--'], db))

