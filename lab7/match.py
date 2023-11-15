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
      #  lst.append(seq[1])
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

def search(pattern, db):
    for item in db: 
        if match(pattern, item):
            lst.append(item)

ass = [['titel', ['--', 'python', '--']]]
cock = ['författare', ['jesus', 'anden', 'zelle']]

# ['jesus', 'anden', 'zelle'], ['--', 'zelle']

# if match(['jesus','zelle']): return true
# elif not seq return false
# else match(['anden', 'zelle'], ['--','zelle'])
seq1 = [['författare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction',
'to', 'computer', 'science']], ['år', 2010]]  
pattern1 = [['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']]

seq2 = [['titel', ['python',], ['år', 2010]]]
seq3 = [[['python']], ['år', '&']]

match(seq1, pattern1)
