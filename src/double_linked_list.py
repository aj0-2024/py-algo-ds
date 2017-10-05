"""
Double Linked List

NULL -> Node1 <-> Node2 <-> Node3 <-> Node4 -> NULL

"""

class Node:
    """Double linked list consists of nodes with value, 
    reference to the previous node and reference to the next node"""
    def __init__(self, value, prevNode, nextNode):
        self.value = value
        self.prev = prevNode
        self.next = nextNode


class DoubleLinkedList:
    """Double linked list datastructure and methods"""
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    # O(1)
    def insert(self, value):
        """Insert the value into the double linked list"""