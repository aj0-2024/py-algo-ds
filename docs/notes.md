# Data Structures, Algorithms & Classic Problems

- [Data Structures, Algorithms & Classic Problems](#data-structures-algorithms--classic-problems)
  - [Data structures](#data-structures)
    - [Linear Data Structures](#linear-data-structures)
    - [Non-Linear Data Structures](#non-linear-data-structures)
      - [Graph](#graph)
  - [Algorithms](#algorithms)
    - [Sorting Algorithms](#sorting-algorithms)
    - [Graph Algorithms](#graph-algorithms)
      - [Breadth First Search](#breadth-first-search)
        - [Algorithm](#algorithm)
      - [Dijkstra's Algorithm](#dijkstras-algorithm)
        - [Algorithm](#algorithm-1)
        - [Notes](#notes)
  - [Classic Problems](#classic-problems)

## Data structures

A Data Structure is a collection of data in a specific format. Each problem and the algorithm to solve the problem require a specific set of actions and choosing a correct data structure for the algorithm will make the actions faster (runtime complexity) while consuming less space (space complexity).

### Linear Data Structures

- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Priority Queue

### Non-Linear Data Structures

- Graph
- Tree
- Trie

#### Graph

Graphs are ADT that have nodes and edges. Edges describe the relationship between the nodes.

- Directed graphs (Edges have a direction)
- Undirected graphs (Edges do not have a direction)
- Weighted graphs (Edges have a value assigned to them)
- Unweighted graphs (Edges do not have any values associated with them)

Trees are special kinds of graphs (No cycles)

---

## Algorithms

Algorithm is a predefined set of steps to reach a solution to a given problem

### Sorting Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Quick Sort
- Merge Sort

---

### Graph Algorithms

| Algorithm Name       | -   |
| -------------------- | --- |
| Breadth First Search | -   |
| Dijkstra's Algorithm | -   |

#### Breadth First Search

Primarily used to answer the following questions

1. Quickly find if a node exists in a graph
2. Quickly find the 'shortest path' between two nodes (least number of edges)

##### Algorithm

1. Store all the connected nodes of the given node in a queue, track all the visited nodes in a hash-table
2. For each item in the queue check if its has already been visited
3. If its a new node that has not been visited, check if it is the desired node
4. If the current node is not the desired node, add the connected nodes (that are not yet visited) of the current node into the queue
5. Keep repeating until queue is empty

---

#### Dijkstra's Algorithm

Algorithm to find the shortest path in a weighted graph

weights
: Each edge of the graph has a value associated with it

##### Algorithm

1. Find the lowest cost node in the graph or the closest node to the start
2. Update costs for its connected nodes
3. If any costs are updated, update the parent node
4. Track all the processed nodes and repeat if there are unprocessed nodes

##### Notes

- Cannot use Dijkstra's algorithm if there are negative-weight edges ( Use Bellman-Ford Algorithm )
- Use the cheapest node on the graph and figure out how long it takes to get to nodes from there

---

## Classic Problems

- Towers of Hanoi
- Knapsack Problem
- Longest Common Substring
