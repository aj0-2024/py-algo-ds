"""Algorithm to invert a binary tree"""
import unittest

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_binary_tree_recursive(tree):
    """Recursive implementation of the binary tree inversion algorithm"""

    if not tree:
        return

    if tree.left:
        invert_binary_tree_recursive(tree.left)

    if tree.right:
        invert_binary_tree_recursive(tree.right)

    tree.left, tree.right = tree.right, tree.left
    return tree
    

if __name__ == "__main__":
    unittest.main()
