class Node:

    def __init__(self, value, next_node):
        """Value can be anything - str, char, number etc. Next node can be instance of a node or Null"""
        self.__value = value
        self.__next = next_node

    @property
    def next():
        return self.__next

    @property
    def value():
        return self.__value
    
    def set_next(node):
        self.__next = node

def create_node(value, next_node):
    """Factory function to create a node with a value"""
    if isinstance(next_node, Node) or next_node == None:
        return Node(value, next_node)
    else:
        raise Exception('Next node has to be instance of class Node')

class LinkedList:

    def __init__(self):
        self.__head = None

    def append(self, value):
        """O(n) method as it requires us to touch all nodes in the list"""
        if (self.__head == None):
            self.__head = create_node(value, None)
        else:
            curr_node = self.__head
            # loop until you reach the end
            while(curr_node != None):
                curr_node = curr_node.next
            curr_node.next = create_node(value, None)
            

    def prepend(self, value):
        """Prepend is very fast"""
        if (self.__head == None):
            self.__head = create_node(value, None)
        else:
            new_node = create_note(value, self.__head)
            self.__head = new_node

    def remove_values(self, value):
        """Be careful when removing head node"""
        if (self.__head == None):
            return
        else:
            # head is valid node so continue
            
        if (self.__head.value == value):
            self.__head = self.__head.next
        else:
            curr_node = self.__head
            next_node = self.__head.next
            while(next_node != None):
                if (next_node.value == value):
                    curr_node.next = next_node.next
                else:
                    # not the intended node
                curr_node = next_node
                next_node = next_node.next
            
            
                
            
