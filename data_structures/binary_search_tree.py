"""
A binary search tree is a tree where every node has 0 to 2 child nodes and follow a
specific property.

Left <= Root <= Right

"""

class TreeNode:
    """Tree implementation"""

    def __init__(self, value):
        self.__val = value
        self.__left = None
        self.__right = None

    def insert(self, val):
        """Insert a value into the BST"""

        if val <= self.__val:
            if self.__left is None:
                self.__left = TreeNode(val)
            else:
                return self.__left.insert(val)
        else:
            if self.__right is None:
                self.__right = TreeNode(val)
            else:
                return self.__right.insert(val)

    def contains(self, val) -> bool:
        """Checks if a value exists within the tree"""

        if val == self.__val:
            return True
        elif val < self.__val:
            if self.__left is not None:
                return self.__left.contains(val)
            else:
                return False
        else:
            if self.__right is not None:
                return self.__right.contains(val)
            else:
                return False

    def print_in_order(self):
        """In order traveral is natural for BST. Left -> Node -> Right"""
        if self.__left is not None:
            self.__left.print_in_order()
        print('{0}'.format(self.__val), end="->")
        if self.__right is not None:
            self.__right.print_in_order()

    def print_pre_order(self):
        """Pre order traversal Node -> Left -> Right"""
        print('{0}'.format(self.__val), end="->")
        if self.__left is not None:
            self.__left.print_pre_order()
        if self.__right is not None:
            self.__right.print_pre_order()

    def print_post_order(self):
        """Post order traversal Left -> Right -> Node"""
        if self.__left is not None:
            self.__left.print_post_order()
        if self.__right is not None:
            self.__right.print_post_order()
        print('{0}'.format(self.__val), end="->")

def test_tree_traversal():
    """Test the tree implementation for simple cases"""

    tree = TreeNode(5)
    tree.insert(1)
    tree.insert(10)
    tree.insert(3)
    tree.insert(2)
    tree.insert(7)
    tree.insert(8)
    tree.insert(4)
    tree.insert(9)
    tree.insert(6)

    print('--In-Order--')
    tree.print_in_order()
    print(' ')
    print('--Pre-Order--')
    tree.print_pre_order()
    print(' ')
    print('--Post-Order--')
    tree.print_post_order()
    print(' ')
    return tree

if __name__ == '__main__':
    test_tree_traversal()
