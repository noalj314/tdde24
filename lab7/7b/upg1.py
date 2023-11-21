from help_functions import *

def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif is_leaf(tree):
        return leaf_fn(tree)
    else:
        left_value = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        right_value = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        
        return inner_node_fn(tree_key(tree), left_value, right_value)

def value_of_tree(tree):
    def empty_tree_fn():
     return 0

    def leaf_fn(key):
        return key**2

    def inner_node_fn(key, left_value, right_value):
        return key + left_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def contains_key(key, tree):
    def empty_tree_fn():
        return False
    def leaf_fn(leaf):
        return key == leaf
    def inner_node_fn(middle, left_value, right_value):
        return key == middle or left_value or right_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_size(tree):
    def empty_tree_fn():
        return 0
    def leaf_fn(leaf):
        return 1 
    def inner_node_fn(middle, left_value, right_value):
        return 1 + left_value + right_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

def tree_depth(tree):
    def empty_tree_fn():
        return 0
    def leaf_fn(leaf):
        return 1
    def inner_node_fn(middle, left_value, right_value):
        return 1 + max(left_value, right_value)
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


# print(contains_key(6, [6, 7, 8]))

# print(contains_key(2, [6, 7, [[2, 3, 4], 0, []]]))

# print(contains_key(2, [[], 1, 5]))

print(tree_size([2, 7, []]))

print(tree_size([]))

print(tree_size([[1, 2, []], 4, [[], 5, 6]]))

print(tree_depth(9))

print(tree_depth([1, 5, [10, 7, 14]]))