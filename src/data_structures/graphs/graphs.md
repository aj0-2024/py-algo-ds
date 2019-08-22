# Graph

Graphs are ADT that have nodes and edges. Edges describe the relationship between the nodes.

There are two kinds of graphs

- Directed graphs (Edges have a direction)
- Undirected graphs (Edges do not have a direction)

Trees are special kinds of graphs (No cycles)

## Breadth First Search

Primarily used to answer the following questions

1. Quickly find if a node exists in a graph
2. Quickly find the 'shortest path' between two nodes

### Algorithm

1. Store all the connected nodes of the given node in a queue, track all the visited nodes in a hash-table
2. For each item in the queue check if its has already been visited
3. If its a new node that has not been visited, check if it is the desired node
4. If the current node is not the desired node, add the connected nodes (that are not yet visited) of the current node into the queue
5. Keep repeating until queue is empty
