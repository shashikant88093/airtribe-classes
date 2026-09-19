# Graphs
Graphs are a fundamental data structure in computer science, used to represent relationships between objects. They consist of nodes (or vertices) and edges connecting them. Graphs can be directed or undirected, weighted or unweighted, and can be used to model a wide variety of problems, from social networks to transportation systems.

## Types of Graphs
1. **Directed Graphs**: In directed graphs, edges have a direction, indicating a one-way relationship between nodes.
2. **Undirected Graphs**: In undirected graphs, edges represent a two-way relationship between nodes.
3. **Weighted Graphs**: In weighted graphs, edges have associated weights, representing costs or distances.
4. **Unweighted Graphs**: In unweighted graphs, all edges are treated equally, without any weights.

## Graph Representation
Graphs can be represented in several ways:
1. **Adjacency Matrix**: A 2D array where the cell at row i and column j indicates the presence (and possibly the weight) of an edge from node i to node j.
2. **Adjacency List**: A list where each index represents a node and contains a list of its neighbors (and possibly the weights of the edges).

## Graph Traversal
Common algorithms for traversing graphs include:
1. **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
2. **Breadth-First Search (BFS)**: Explores all neighbors at the present depth before moving on to nodes at the next depth level.

## Applications of Graphs
Graphs are used in various applications, including:
- Social network analysis
- Web page ranking (e.g., PageRank)
- Route planning and navigation
- Network topology and design

Understanding graphs and their properties is essential for solving complex problems in computer science and related fields.



## Graph ( Cyclic and Acyclic   )
Graphs can be classified into two main categories: cyclic and acyclic.

1. **Cyclic Graphs**: A graph is considered cyclic if it contains at least one cycle, which is a path that starts and ends at the same node without traversing any edge more than once. Cyclic graphs can be directed or undirected.

2. **Acyclic Graphs**: A graph is acyclic if it does not contain any cycles. A special type of acyclic graph is the Directed Acyclic Graph (DAG), which is a directed graph that has no cycles. DAGs are commonly used to represent dependencies, such as task scheduling and version control systems.  

## Graph ( Weighted and Unweighted )
Graphs can also be classified based on the weights of their edges:

1. **Weighted Graphs**: In weighted graphs, edges have associated weights, which can represent costs, distances, or other metrics. Algorithms for weighted graphs, such as Dijkstra's and Bellman-Ford, take these weights into account when finding paths.

2. **Unweighted Graphs**: In unweighted graphs, all edges are treated equally, without any weights. Algorithms for unweighted graphs, such as BFS, can be more efficient since they do not need to consider edge weights.

## Graph ( Connected and Disconnected )
Graphs can also be classified based on their connectivity:

1. **Connected Graphs**: A graph is connected if there is a path between every pair of vertices. In other words, all nodes are reachable from any starting node.

2. **Disconnected Graphs**: A graph is disconnected if there are at least two vertices in the graph that are not connected by a path. Disconnected graphs can be divided into multiple connected components.


## How to store a graph

Graphs can be stored in various ways, depending on the requirements of the application and the specific operations that need to be performed. The two most common representations are:

1. **Adjacency Matrix**: This is a 2D array where the cell at row i and column j indicates the presence (and possibly the weight) of an edge from node i to node j. This representation is simple and allows for quick lookups, but it can be memory-intensive for large, sparse graphs.
    
    Example of an adjacency matrix for a graph with 4 nodes (0, 1, 2, 3):
    ```
    0 1 2 3
    0 0 1 0 1
    1 1 0 1 0
    2 0 1 0 1
    3 1 0 1 0
    ```

2. **Adjacency List**: This is a list where each index represents a node and contains a list of its neighbors (and possibly the weights of the edges). This representation is more memory-efficient for sparse graphs and allows for easy iteration over the neighbors of a node.
    
    Example of an adjacency list for the same graph:
    ```
    0: [1, 3]
    1: [0, 2]
    2: [1, 3]
    3: [0, 2]
    ```


Other representations, such as edge lists or incidence matrices, can also be used depending on the specific needs of the application.


## How ( Degree of a vertex )
The degree of a vertex in a graph is the number of edges connected to it. In directed graphs, we distinguish between in-degree (the number of incoming edges) and out-degree (the number of outgoing edges). The degree of a vertex can provide insights into its connectivity and importance within the graph.