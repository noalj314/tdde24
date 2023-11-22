def is_empty_tree(tree):
    """Returns boolean value depending on if given tree is empty"""
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    """Returns boolean value depending on if given argument is integer"""
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    """Creates a list with the structure of a tree with given arguments"""
    return [left_tree, key, right_tree]

	
def left_subtree(tree):
    """Returns the left subtree of given tree"""
    return tree[0]


def right_subtree(tree):
    """Returns the right subtree of given tree"""
    return tree[2]
    
def tree_key(tree):
    """Returns the key value of given tree"""
    return tree[1]