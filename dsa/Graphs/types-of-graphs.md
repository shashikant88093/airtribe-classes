# Directed Graphs

- Direction Associated with Edges: In directed graphs, edges have a specific direction, indicating a one-way relationship between nodes. This is represented by an arrow pointing from the source node to the destination node.
- Representation: Directed graphs can be represented using an adjacency list or an adjacency matrix, where the direction of edges is taken into account. In an adjacency list, each node points to a list of its outgoing edges, while in an adjacency matrix, the presence of an edge from node i to node j is indicated by a non-zero value in the cell at row i and column j.
- Applications: Directed graphs are commonly used in scenarios where relationships have a specific direction, such as in social networks (e.g., following relationships), web page ranking (e.g., PageRank), and task scheduling (e.g., representing dependencies between tasks).


```
example of a directed graph in diagram form:

```
     A → B
     ↓   ↑
     C → D


# undirected Graphs

- No Direction Associated with Edges: In undirected graphs, edges do not have a specific direction, indicating a two-way relationship between nodes. This is represented by a line connecting the nodes.
- Representation: Undirected graphs can be represented using an adjacency list or an adjacency matrix, where the direction of edges is not taken into account. In an adjacency list, each node points to a list of its neighboring nodes, while in an adjacency matrix, the presence of an edge between node i and node j is indicated by a non-zero value in the cell at row i and column j.
- Applications: Undirected graphs are commonly used in scenarios where relationships are symmetric, such as in social networks (e.g., friendship relationships), map representation (e.g., roads between cities), and molecular structure modeling (e.g., bonds between atoms).

```
example of an undirected graph in diagram form:

     A — B
     |   |
     C — D




# Cyclic Graphs

- Presence of Cycles: A cyclic graph contains at least one cycle, which is a path that starts and ends at the same node without traversing any edge more than once. Cycles can be present in both directed and undirected graphs.
- Representation: Cyclic graphs can be represented using an adjacency list or an adjacency matrix, similar to other types of graphs. The presence of cycles can be detected using algorithms such as Depth-First Search (DFS) or Breadth-First Search (BFS).
- Applications: Cyclic graphs are commonly used in scenarios where feedback loops or repeated processes are present, such as in electrical circuits, transportation networks, and social networks.

```
example of a cyclic graph in diagram form:

     A → B
     ↑   ↓
     D ← C


# Acyclic Graphs

- Absence of Cycles: An acyclic graph does not contain any cycles. A special type of acyclic graph is the Directed Acyclic Graph (DAG), which is a directed graph that has no cycles. DAGs are commonly used to represent dependencies, such as task scheduling and version control systems.
- Representation: Acyclic graphs can be represented using an adjacency list or an adjacency matrix, similar to other types of graphs. The absence of cycles can be verified using algorithms such as topological sorting or cycle detection algorithms.
- Applications: Acyclic graphs are commonly used in scenarios where dependencies need to be represented, such as in project management (e.g., task dependencies), data processing pipelines, and version control systems (e.g., Git commit history).

```
example of an acyclic graph in diagram form:

     A → B
     ↓   ↓
     C   D


# Weighted Graphs

- Edge Weights: In weighted graphs, edges have associated weights, which can represent costs, distances, or other metrics. The weights can be positive, negative, or zero, depending on the specific application.
- Representation: Weighted graphs can be represented using an adjacency list or an adjacency matrix, where the weights of the edges are stored along with the connections between nodes. In an adjacency list, each node points to a list of its neighboring nodes along with the corresponding edge weights, while in an adjacency matrix, the weights of the edges are stored in the cells of the matrix.
- Applications: Weighted graphs are commonly used in scenarios where the cost or distance of connections between nodes is important, such as in transportation networks (e.g., shortest path algorithms), network routing (e.g., finding the least-cost path), and resource allocation problems (e.g., minimizing costs in supply chain management).


Weight = distance /cost / time / capacity / etc.



```
example of a weighted graph in diagram form:

     A —(2)→ B
     |       |
    (3)     (1)
     ↓       ↓
     C —(4)→ D

# Unweighted Graphs

- Equal Edge Weights: In unweighted graphs, all edges are treated equally, without any weights. This means that the cost or distance of traversing an edge is the same for all edges in the graph.
- Representation: Unweighted graphs can be represented using an adjacency list or an adjacency matrix, similar to other types of graphs. In an adjacency list, each node points to a list of its neighboring nodes, while in an adjacency matrix, the presence of an edge between node i and node j is indicated by a non-zero value in the cell at row i and column j.
- Applications: Unweighted graphs are commonly used in scenarios where the relationships between nodes are of equal importance, such as in social networks (e.g., friendship relationships), unweighted shortest path problems (e.g., finding the minimum number of edges between nodes), and connectivity analysis (e.g., determining if a network is connected).

```
example of an unweighted graph in diagram form:
        A — B
        |   |
        C — D



## How to store a graph :-

## Adjacency Matrix
- Representation: An adjacency matrix is a 2D array where the cell at row i and column j indicates the presence (and possibly the weight) of an edge from node i to node j. This representation is simple and allows for quick lookups, but it can be memory-intensive for large, sparse graphs.
- Example: For a graph with 4 nodes (0, 1, 2, 3), the adjacency matrix can be represented as follows:
```
    0 1 2 3
    0 0 1 0 1
    1 1 0 1 0
    2 0 1 0 1
    3 1 0 1 0
```

## Adjacency List
- Representation: An adjacency list is a list where each index represents a node and contains a list of its neighbors (and possibly the weights of the edges). This representation is more memory-efficient for sparse graphs and allows for easy iteration over the neighbors of a node.
- Example: For the same graph, the adjacency list can be represented as follows:
```
    0: [1, 3]
    1: [0, 2]
    2: [1, 3]
    3: [0, 2]
```



- **Graphs and trees:** Every tree is a graph, but not every graph is a tree.

- **Graphs can have cycles:** A graph can contain cycles, which are paths that start and end at the same node without traversing any edge more than once. Trees, on the other hand, are acyclic by definition.

- **Tree can't be cyclic:** Trees are a special type of graph that is acyclic and connected. They do not contain any cycles, and there is exactly one path between any two nodes in a tree.

- **Thats Why trees are a subset of graphs:** Since trees are a specific type of graph that satisfies certain properties (acyclic and connected), they can be considered a subset of graphs. All trees are graphs, but not all graphs are trees.


## Degree of a graph
- **Definition:** The degree of a vertex in a graph is the number of edges incident to that vertex. In directed graphs, we can distinguish between in-degree (the number of incoming edges) and out-degree (the number of outgoing edges). The degree of a vertex can provide insights into its connectivity and importance within the graph.

Degree = Number of incoming edges + Number of outgoing edges

```
Example: For a directed graph with the following edges:
    A → B
    A → C
    B → C
    C → A
The degrees of the vertices are as follows:
    Vertex A: In-degree = 1 (from C), Out-degree = 2 (to B and C), Total degree = 3
    Vertex B: In-degree = 1 (from A), Out-degree = 1 (to C), Total degree = 2
    Vertex C: In-degree = 2 (from A and B), Out-degree = 1 (to A), Total degree = 3
```


## Components of a graph
- **Definition:** A component of a graph is a maximal connected subgraph, meaning that it is a connected subgraph that cannot be extended by including any adjacent vertex. In other words, a component is a subset of vertices and edges in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.

``` 
Example: Consider the following undirected graph:
    A — B   C — D
    |       |
    E       F
In this graph, there are two components:
1. Component 1: {A, B, E} - This component includes vertices A, B, and E, which are all connected to each other.
2. Component 2: {C, D, F} - This component includes vertices C, D, and F, which are all connected to each other. There are no edges connecting vertices from Component 1 to Component 2, so they are separate components.
``` 


```
Example in python code for finding components of a graph using Depth-First Search (DFS):

```python
def dfs(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)    



def find_components(graph):
    visited = set()
    components = []
    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)
    return components   

# Example usage:
graph = {
    'A': ['B', 'E'],
    'B': ['A'],
    'C': ['D', 'F'],
    'D': ['C'],
    'E': ['A'],
    'F': ['C']
}
components = find_components(graph)
print("Components of the graph:", components)
```

## Common way to store the graph in computer memory:-

- Adjacency Matrix: A 2D array where the cell at row i and column j indicates the presence (and possibly the weight) of an edge from node i to node j. This representation is simple and allows for quick lookups, but it can be memory-intensive for large, sparse graphs.
  - Example of an adjacency matrix for a graph with 4 nodes (0, 1, 2, 3):
  ```
  0 1 2 3
  0 0 1 0 1
  1 1 0 1 0     
    2 0 1 0 1
    3 1 0 1 0


- Adjacency List: A list where each index represents a node and contains a list of its neighbors (and possibly the weights of the edges). This representation is more memory-efficient for sparse graphs and allows for easy iteration over the neighbors of a node.
  - Example of an adjacency list for the same graph:
  ```
  0: [1, 3]
  1: [0, 2]
  2: [1, 3]
  3: [0, 2] 


