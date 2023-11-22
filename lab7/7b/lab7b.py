from help_functions import *

def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """Traverses a tree structure and applies functions based on node types"""
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif is_leaf(tree):
        return leaf_fn(tree)
    else:
        left_value = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        right_value = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        return inner_node_fn(tree_key(tree), left_value, right_value)

def value_of_tree(tree):
    """Returns sum of key and values of left nodes squared"""
    def empty_tree_fn():
        """Returns 0"""
        return 0
    def leaf_fn(key):
        """Returns key value squared"""
        return key**2
    def inner_node_fn(key, left_value, right_value):
        """"Returns sum of key- and left-value"""
        return key + left_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def contains_key(key, tree):
    """Returns a boolean value """
    def empty_tree_fn():
        """Returns false"""
        return False
    def leaf_fn(leaf):
        """Returns boolean value depending on key and leaf values"""
        return key == leaf
    def inner_node_fn(middle, left_value, right_value):
        """Returns boolean value depending on key- and subtree-values"""
        return key == middle or left_value or right_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_size(tree):
    """Returns the size of the tree"""
    def empty_tree_fn():
        """Returns 0 if tree is empty"""
        return 0
    def leaf_fn(leaf):
        """Returns 1 if node is a leaf"""
        return 1 
    def inner_node_fn(middle, left_value, right_value):
        """Returns the amount of all the inner nodes"""
        return 1 + left_value + right_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_depth(tree):
    """Returns the depth of the tree"""
    def empty_tree_fn():
        """Returns 0 if tree is empty"""
        return 0
    def leaf_fn(leaf):
        """Returns 1 if tree is a leaf"""
        return 1
    def inner_node_fn(middle, left_value, right_value):
        """Returns the maximum depth between left and right value"""
        return 1 + max(left_value, right_value)
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

