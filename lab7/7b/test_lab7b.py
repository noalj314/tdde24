import unittest
from lab7b import *


class test(unittest.TestCase):
    """Tests for tree operations including value calculation, key existence, size, and depth."""
    
    def test_value_of_tree(self):
        """Tests correct value calculation of different tree structures."""
        self.assertEqual(value_of_tree([6, 7, 8]), 43)
        self.assertEqual(value_of_tree([[], 7, []]),7)
        self.assertEqual(value_of_tree([[[[], 2, []], 3, []], 4, []]),9 ) # 4 + 3 + 4
        self.assertEqual((value_of_tree([[[[1,0,[]],2,1],4,1],7,5])), 14)
        self.assertNotEqual(value_of_tree([[[[1,0,[]],2,1],4,1],7,5]),15)


    def test_contains_key(self):
        """Tests if specified keys are correctly identified in trees."""
        self.assertTrue(contains_key(6, [6, 7, 8]))
        self.assertTrue(contains_key(7, [[], 7, []]))
        self.assertTrue(contains_key(2, [6, 7, [[2, 3, 4], 0, []]]))
        self.assertTrue(contains_key(2, [[[2, 3, 4], 0, []], 7, [[1, 3, 4], 0, []]]))
        self.assertFalse(contains_key(2, [6, 7, 8]))
        self.assertFalse(contains_key(9, [6, 7, [[2, 3, 4], 0, []]]))
        self.assertFalse(contains_key(8, [[[2, 3, 4], 0, []], 7, [[1, 3, 4], 0, []]]))
        self.assertTrue(contains_key(2, [[],2,[]]))


    def test_tree_size(self):
        """Tests for correct tree size calculation."""
        self.assertTrue(tree_size([2, 7, []]) == 2)
        self.assertTrue(tree_size([]) == 0)
        self.assertTrue(tree_size([[1, 2, []], 4, [[], 5, 6]]) == 5)
        self.assertFalse(tree_size([[1, 2, []], 4, [[], 5, 6]]) == 3)
        self.assertNotEqual(tree_size([]), 3, "")


    def test_tree_depth(self):
        """Tests for accurate tree depth"""
        self.assertTrue(tree_depth(9) == 1)
        self.assertTrue(tree_depth([1, 5, [10, 7, 14]]) == 3)
        self.assertFalse(tree_depth([1, 5, [10, 7, 14]]) == 5)
        self.assertFalse(tree_depth([[[2, 3, 4], 0, []], 7, [[1, 3, 4], 0, []]]) == 5)
        

if __name__ == '__main__':
    unittest.main()

