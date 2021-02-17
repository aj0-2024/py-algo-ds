# Python Algorithms and Data structures

Welcome ! This repository contains notes & implementations of various data structures & algorithms. 

> Many algorithms are simple, clear & thought provoking. Some of them are extremely beautiful and mesmerizing.

Purely for educational purpose and not intended for any other use.

- [Python Algorithms and Data structures](#python-algorithms-and-data-structures)
  - [Algorithm Status Table](#algorithm-status-table)
  - [Data structures Status Table](#data-structures-status-table)
  - [Algorithm Review Table](#algorithm-review-table)
  - [Problem sets](#problem-sets)
    - [Searching](#searching)
    - [Basic Sorting](#basic-sorting)
    - [Recursion](#recursion)
    - [Dynamic Programming](#dynamic-programming)
    - [Divide & Conquer](#divide--conquer)
    - [Greedy approach](#greedy-approach)
    - [Iterative approach](#iterative-approach)
  - [TO-DO](#to-do)
  
## Algorithm Status Table
| # | Algorithm Name | Status | 
| -- | -- | -- |
| 1 | Bubble Sort | ✔︎ |
| 2 | Selection Sort | ✔︎ |
| 3 | Insertion Sort | ✔︎ |
| 4 | Heap Sort | 𐄂 |
| 5 | Merge Sort | ✔︎ | 
| 6 | Quick Sort | ✔︎ |
| 7 | Topological Sort | 𐄂 |
| 8 | Depth First Search | ✔︎ |
| 9 | Breadth First Search | ✔︎ |
| 10 | A\* Search | 𐄂 |
| 11 | Binary Search | ✔︎ |
| 12 | Tree Traversals (Pre-Order, Post-Order & In-Order) | ✔︎ |
| 13 | Maximum Subarray Problem | ✔︎ |
| 14 | Lee's Algorithm | 𐄂 |
| 15 | Flood Fill Algorithm | 𐄂 | 
| 16 | Floyd Cycle Detection Algorithm | ✔︎ |
| 17 | Longest Increasing Subsequence | 𐄂 |
| 18 | Union Find Algorithm | 𐄂 |
| 19 | Kruskal's Algorithm | 𐄂 | 
| 20 | Floyd Warshall's Algorithm | 𐄂 |
| 21 | Huffman Coding Compression | 𐄂 |
| 22 | Euclid's Algorithm for GCD | 𐄂 |
| 23 | Primality Tests | ✔︎ |
| 24 | Boyer Moore Majority Vote Algorithm | 𐄂 |
| 25 | Fisher-Yates Shuffle Algorithm | ✔︎ |
| 26 | Fibonacci Series | ✔︎ |
| 27 | Bellman Ford Algorithm | ✔︎ |
| 28 | Number of ways to make change | ✔︎ |
| 29 | Knapsack 0/1 | ✔︎ |
| 30 | Levenshtein Distance | ✔︎ |
| 31 | Matrix Search | ✔︎ |
| 32 | Find Rotation Point | 𐄂 |
| 33 | Find Duplicate Integer | ✔︎ |
| 34 | Towers of Hanoi | ✔︎ |

## Data structures Status Table

| # | Data Structure | Status |
| -- | -- | -- |
| 1 | Array | 𐄂 |
| 2 | Vector Array/List | 𐄂 |
| 3 | Linked List (Single, Double) | ✔︎ |
| 4 | Binary Search Tree | ✔︎ |
| 5 | Min Heap & Max Heap | ✔︎ | 
| 6 | Stack | ✔︎ |
| 7 | Queue | ✔︎ |
| 8 | Dequeue | 𐄂 |
| 9 | Priority Queue | 𐄂 |
| 10 | Unweighted Graph | 𐄂 |
| 11 | Weighted Graph | 𐄂 |
| 12 | Trie | 𐄂 |
| 13 | Hash Set | 𐄂 |
| 14 | Hash Table | 𐄂 |
| 15 | LSM Tree | 𐄂 |
| 16 | B Tree | 𐄂 |
| 17 | AVL Tree | 𐄂 |
| 18 | Ternanry Search Tree | 𐄂 |
| 19 | Bloom Filter | 𐄂 |

## Algorithm Review Table
| # | Algorithm | Num Reviewed | 
| -- | -- | -- |
| 1 | Searching | 4 |
| 2 | Basic Sorting | 3 |
| 3 | Dynamic Programming | 5 |
| 4 | Divide & Conquer | 2 |
| 5 | Recursion | 1 |
| 6 | Iteration | 0 |
| 7 | Greedy Approach | 3 |
| 8 | Matrix Problems | 1 |
| 9 | Array Problems | 0 |
| 10 | Tree Problems | 2 |
| 11 | Geometry Problems | 0 |
| 12 | Bit manipulation Problems | 2 |
| 13 | String Problems | 0 |
| 14 | Probability Problems | 0 |
| 15 | Graph Problems | 0 |
| 16 | Math Problems | 0 |
| 17 | Sliding Window Problems | 0 |

## Data structure review table
| # | Data Structure | Num Reviewed |
| -- | -- | -- |
| 1 | Binary Search Tree | 0 |
| 2 | Linked List | 0 |
| 3 | Stack | 0 |
| 4 | Queue | 0 |
| 6 | Heap | 0 |

## Categories

### Searching 
| # | Problem |
| --- | --- |
| 1 | Binary Search |
| 2 | Depth First Search |
| 3 | Breadth First Search |
| 4 | Matrix Search |

### Basic Sorting
| # | Problem |
| --- | --- |
| 1 | Bubble Sort |
| 2 | Insertion Sort |
| 3 | Selection Sort |


### Recursion 
| # | Problem |
| --- | --- |
| 1 | Tree traversals |
| 2 | Binary tree inversion |
| 3 | Binary tree diameter |
| 4 | Permutations |
| 5 | Powerset |
| 6 | Towers of hanoi |
| 7 | Max path sum of a Binary tree |

#### Notes
- Runtime complexity = O(k ^ n) where k = number of branches per each call.

### Iteration
| # | Problem |
| --- | --- |
| 1 | In order traversal |

### Dynamic Programming 
| # | Problem |
| --- | --- |
| 1 | Fibonacci series |
| 2 | Making change with denominations |
| 3 | Minimum number of coins |
| 4 | Knapsack 0/1 |
| 5 | Levenshtein Distance | 
| 6 | Staircase Traversal |
| 7 | Max Sum Increasing Subsequence |

#### Notes
- Often slower, a faster but less accurate algorithm may exist.

#### Notes
- Base case
- Start from minimum
- What to do at each step? how do we update?

### Divide & Conquer 
| # | Problem |
| --- | --- |
| 1 | Maximum subarray problem |
| 2 | Quick sort |
| 3 | Merge sort |

### Greedy approach
| # | Problem |
| --- | --- |
| 1 | Kadane's algorithm |
| 2 | Highest product of 3 |
| 3 | Product of all other numbers |
| 4 | Sunset Views |
| 5 | Merging meeting time |
| 6 | Apple Stocks |

#### Notes
- Not always accurate so be careful.
- Next step to consider is Dynamic Programming.

### Matrix Problems
| # | Problem |
| --- | --- |
| 1 | River Sizes |
| 2 | Remove Islands |

### Array Problems
| # | Problem |
| --- | --- |
| 1 | Find duplicate number |
| 2 | Merge meeting times |
| 3 | Reverse string in place |
| 4 | Reverse words in place |
| 5 | Longest Peak |
| 6 | Minimum change you cannot make |

### String Problems 
| # | Problem |
| --- | --- |
| 1 | String Permutation |
| 2 | Word Cloud |
| 3 | Longest Palindrome String |
| 4 | Group Anagrams |
| 5 | IP Addresses |

### Tree Problems
| # | Problem |
| --- | --- |
| 1 | Youngest common ancestor |
| 2 | Valid Binary Search Tree |
| 3 | Second Largest Item in BST |
| 4 | Find closeset value in BST |
| 5 | Calculate Branch Sums |
| 6 | Calculate Node Depths |
| 7 | Min-Height BST |
| 8 | Invert Binary Tree |
| 9 | Binary Tree Diameter |
| 10 | Max path sum |

### Geometry Problems
| # | Problem |
| --- | --- |
| 1 | Recentagle interception problem |

### Bit Manipulation Problems
| # | Problem |
| --- | --- |
| 1 | Drone problem |

### Probability Problems |
| # | Problem |
| --- | --- |
| 1 | In-Place Shuffle |
| 2 | 5-Sided die & 7-Sided die |

### Graph Problems
| # | Problem |
| --- | --- |
| 1 | Graph Coloring |
| 2 | Mesh Message |

### Math Problems
| # | Problem |
| --- | --- |
| 1 | Two Egg Problem |

### Sliding Window Problems 
| # | Problem |
| --- | --- |
| 1 | Staircase Traversal |

### Traversal Problems
| # | Problem |
| --- | --- |
| 1 | Zigzag Traversal |

## Complex Run-time analysis
| # | Problem Set |
| --- | --- |
| 1 | String Problems |
| 2 | Graph Problems |
| 3 | Dynamic Programming |

## Common Mistakes
| # | Description | Num times |
| --- | --- | --- |
| 1 | Off by one error | 2 |
| 2 | Input validation (Checks for empty) | 1 |
| 3 | Improper initialization values | 1 |
| 4 | Incompletely updating temporary variables | 1 |
| 5 | Improper Input Validation | 1 |
| 6 | Sending wrong arguements or in a wrong order | 1 |
| 7 | Infinite while loops | 1 |
| 8 | Understanding the question wrong | 1 |
| 9 | Not considering that array may have duplicate numbers within range | 1 |

## Unique looping problems
| # | Problem | Description |
| --- | --- |
| 1 | Valid IP addresses from a string | Looping based on groups of 4 |
| 2 | Four Number Sum | Two inner loops ...i and i... which do different things |

## TO-DO
- Implement the tree traversals (recursive & iterative in a separate file)
- Finish `Find rotation point`
