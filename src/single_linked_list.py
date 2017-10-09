"""
Single Linked List

When to use ?
1. When you want an insert into the beginning of the list quickly

When not to use ?
1. Linked list needs more memory than array, so if memory is a concern then better to choose array over linked list
   Linked list needs more memory for storing references
"""

class Node:
    """Node contains value and reference to the next node"""
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node

class SingleLinkedList:
    """Linked list is useful for efficient add at the first"""
    def __init__(self):
        self._head = None
        self._size = 0

    def insert_at_start(self, value):
        """Insert value into the head of the linked list"""
        if self._head is None:
            new_node = Node(value, None)
            self._head = new_node
        else:
            new_node = Node(value, self._head)
            self._head = new_node
            self._size += 1

    def insert_at_end(self, value):
        """Insert value into the tail of the linked list"""

    def insert(self, atNode, value):
        """Insert value at node"""

    def traverse_list(self):
        """Traverse and print out the values in the list"""

    def remove_at_start(self):
        """remove the first node and return it"""

    def remove_at_end(self):
        """Traverse list and remove the tail node and return it"""

    def remove(self, value):
        """Traverse and remove the first encountered value"""

    def has_value(self, value):
        """Traverse and check if the linked list has given value"""
        if self._size == 0:
            return False
        else:
            curr = self._head
            found = False
            while curr is not None:
                if curr.val == value:
                    found = True
                    break
                else:
                    curr = curr.next
            return found

    def to_array(self):
        """Convert the linked list into an array"""

    @property
    def size(self):
        """TODO: Use getter, Get the size of the linked list"""
        return self._size
