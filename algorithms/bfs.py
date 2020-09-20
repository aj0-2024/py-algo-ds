"""
Breadth first search is an algorithm that is useful to find a shortest path given a tree or graph.
BFS uses a queue in its implementation.

Notes:
    1. May use more memory than a DFS search since number of nodes in a level is usually more than
    the height.
"""
import Queue

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root, target):
    """Check if target exists within the tree"""

    queue_to_process = Queue.queue()
    queue_to_process.put(root)

    while not queue_to_process.empty():
        curr_node = queue_to_process.get()

        if curr_node._value == target:
            return True

        if curr_node.left:
            queue_to_process.put(curr_node.left)

        if curr_node.right:
            queue_to_process.put(curr_node.right)

    return False
        

    
