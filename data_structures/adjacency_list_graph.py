"""Adjacency list is a graph representation using array or a hash map"""

class AdjacencyListGraph:
    """Graph representation using dictionary"""

    def __init__(self):
        self.__nodes = {}

    def __str__(self):
        return str(self.__nodes)

    def insert_vertex(self, data):
        """Insert a vertex and its relationships """
        self.__nodes[data] = set()

    def insert_edge(self, start_data, end_data):
        """Insert a relationship b/w edges"""
        adj_list_start = self.__nodes.get(start_data, None)
        adj_list_end = self.__nodes.get(end_data, None)

        if adj_list_start is not None and adj_list_end is not None:
            adj_list_start.add(end_data)
            adj_list_end.add(start_data)
        else:
            raise Exception('vertexes are not found')

def test_adjacency_list_graph():
    """Simple test for the graph implementation"""
    tree = AdjacencyListGraph()

    tree.insert_vertex(0)
    tree.insert_vertex(1)
    tree.insert_vertex(2)
    tree.insert_vertex(3)

    tree.insert_edge(0, 1)
    tree.insert_edge(1, 2)
    tree.insert_edge(1, 3)
    tree.insert_edge(2, 3)

    print(tree)

if __name__ == '__main__':
    test_adjacency_list_graph()

    


        

    

    
