# Encoding: ISO-8859-1
from match import search, match
from books import *
import unittest

from match import search, match
from books import *
import unittest

true_pattern_1 = ['&', 'messi', '--']
false_pattern_2 = ['&', 'messi', 'i', 'jordan', 'rav']
test_pattern3 = [
    [['fÃÂ¶rfattare', ['john', 'zelle']], ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                                                          'computer', 'science']]]]
test_pattern_4 = [['player', ['&', '--']], ['FMVP', ['amount', '&']], ['DPOY', ['amount', '&']],
                  ['chips', ['amount', '&']]]

test_seq_1 = ['ronaldos', 'messi', 'i', 'min']
test_seq_2 = [
    [['player', ['Kawhi', 'Leonard']], ['FMVP', ['amount', 2]], ['DPOY', ['amount', 2]], ['chips', ['amount', 2]]],
    [['player', ['Giannis', 'Antetokounmpo']], ['MVP', ['amount', 2]], ['FMVP', ['amount', 1]], ['DPOY', ['amount', 2]],
     ['chips', ['amount', 1]]],
    [['player', ['Nikola', 'Jokic']], ['MVP', ['amount', 2]], ['FMVP', ['amount', 1]], ['chips', ['amount', 1]]]

]

class test_functions(unittest.TestCase):

    def test_match(self):
        """Test the match function"""
        self.assertTrue(match(test_seq_1, true_pattern_1 ))
        self.assertFalse(match(test_seq_1, false_pattern_2))

    def test_final(self):
        """Test both the match and the search function"""
        lst = []
        for item,ytem in zip(test_seq_2, test_pattern_4): 
            if match(item, ytem):
                lst.append(item)
        return lst
        
if __name__ == '__main__':
    unittest.main()
    