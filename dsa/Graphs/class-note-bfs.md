# Breadth-First Search (BFS) Class Notes

## Session Overview
This session focused on breadth-first search (BFS) and how to use it on graphs and grids.
You’ll see the BFS queue pattern, reachability checks, graph construction from edges, and why BFS is the right tool for shortest-distance and minimum-time problems.
The major applications were Rotting Oranges and 01 Matrix, both solved with multi-source BFS.

## Graph Traversal Foundations
The earlier graph review covered the core building blocks: graph representation, types of graphs, and traversal with DFS and BFS.

DFS was recalled as: visit the source, go to all unvisited neighbors, and repeat from every unvisited vertex.

Key insight: DFS goes deep first through unvisited neighbors, then repeats from every unvisited vertex.

BFS, by contrast, explores level by level, which is why it is so useful for shortest path style questions in unweighted graphs.

Key takeaway: DFS and BFS are different traversal styles, but BFS is the one that naturally models “minimum steps” and “minimum time.”

## Breadth-First Search (BFS) on Graphs
BFS explores a graph in layers. Starting from a source node, it uses a queue so that the oldest discovered node is always processed first.

The class shorthand for the BFS loop was:

Key insight: R M W A S T A R

R = remove from queue
M = mark visited
W = work / print
A S T A R = add star = add all unvisited neighbors
“Star” means unvisited.
The usual BFS pattern is:

Put the source node into a queue
Remove the front node
If it is already visited, skip it
Otherwise:
mark it visited
print/process it
add all unvisited neighbors to the queue
Repeat until the queue is empty
Key insight: BFS may enqueue the same node more than once, so the “already visited” check on removal is essential.

A queue example walked through nodes being discovered and then skipped if they had already been processed. That behavior is normal: duplicate queue entries are fine as long as you skip visited nodes when they come out.

### BFS with an adjacency list
For a graph stored as an adjacency list, BFS can be written like this:

```python
visited = [False] * len(adj_list)
q = deque()
q.append(0)   # start node
answer = []

while len(q) > 0:
    front = q.popleft()   # remove from front
    if visited[front]:
        continue
    visited[front] = True
    answer.append(front)

    for neighbor in adj_list[front]:
        if not visited[neighbor]:
            q.append(neighbor)
```
The important detail is that the node is marked visited when it is processed, not just when it is discovered.

Key insight: continue is for already-visited nodes; marking visited happens only once the node is actually processed.

### Multiple valid BFS orders
A graph does not always have a single unique BFS traversal. If a node has multiple neighbors, the order in which those neighbors are enqueued can change the final traversal order.

Key insight: A graph may have multiple correct BFS orders depending on neighbor ordering.

Key takeaway: BFS traversal order depends on the queue and neighbor ordering, but the level-by-level structure remains the same.

## Reachability in a Graph
A common BFS problem is: given a source and destination, determine whether there is a path from source to destination.

The logic is simple:

start BFS from the source
explore outward through reachable nodes
if you ever encounter the destination, return True
if the queue empties first, return False
This works because BFS explores the connected component containing the source.

### BFS reachability template
```python
visited = [False] * len(adj_list)
q = deque([source])

while q:
    node = q.popleft()
    if visited[node]:
        continue
    visited[node] = True

    if node == destination:
        return True

    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            q.append(neighbor)

return False
```
Key insight: For reachability, you do not need the actual path unless the problem asks for it — just whether the destination is ever reached.

A common pitfall was highlighted: checking visited and marking visited are different steps. Checking prevents repeated work; marking records that the node has now been processed.

Key takeaway: If the destination is reachable, BFS will find it; otherwise, the queue will empty and you return False.

## Building a Graph from Edges
Sometimes the graph is not given as an adjacency list. Instead, you are given just the edges, so you must build the graph first.

For an undirected graph, the pattern is:

```python
graph[u].append(v)
graph[v].append(u)
```
If the graph is directed, you only add one direction.

Key insight: When the input is a list of edges, the first step is usually to convert it into an adjacency list before running BFS or DFS.

This same structure was used for checking whether a destination is reachable from a source.

Key takeaway: Convert edge lists into adjacency lists first; then BFS becomes straightforward.

## Why BFS Is Used for Shortest Path / Minimum Time Questions
BFS is the go-to method when a problem asks for:

shortest path
shortest time
minimum moves
minimum number of edges
This is especially true in unweighted graphs.

Key insight: Whenever you see “shortest” in an unweighted graph, BFS is usually the right tool.

Key takeaway: BFS solves “minimum steps” problems because it expands in increasing distance order.

## LeetCode 994: Rotting Oranges
In Rotting Oranges, the grid contains:

0 = empty cell
1 = fresh orange
2 = rotten orange
A rotten orange infects neighboring fresh oranges in the 4 directions:

up
down
left
right
The infection spreads minute by minute, so this is a classic multi-source BFS problem.

Key insight: Start BFS from all initially rotten oranges at once. Each BFS layer corresponds to 1 minute.

Core strategy
Traverse the grid once
Count the fresh oranges
Put all rotten oranges into the queue with time 0
BFS outward through valid fresh neighbors
Track the maximum time seen
If any fresh orange remains unreachable, return -1
Queue content
Each queue element carries:

(i, j, time)
or equivalently (row, col, time).

That time value tells you when that orange becomes rotten.

BFS process
For each popped orange:

if already visited, skip it
otherwise mark it visited
update the answer with the maximum time seen so far
if it is fresh, decrement fresh count
check its 4 neighbors
if a neighbor is inside bounds, fresh, and unvisited, enqueue it with time + 1
The direction vectors used were:

```python
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
```
Watch out: Always check all three conditions before enqueueing a neighbor:

inside bounds
fresh
not visited
Final answer
If fresh_count == 0 after BFS, return the recorded maximum time
Otherwise return -1
Key insight: The answer is the last minute at which a fresh orange turns rotten, not the first.

Common pitfalls
Forgetting to use multi-source BFS
Forgetting the time field in queue entries
Forgetting to decrement fresh_count
Forgetting to return -1 when some fresh oranges are unreachable
Forgetting the visited check, which can cause repeated queue entries
Key takeaway: Rotting Oranges is a multi-source BFS where the answer is the maximum time needed for rot to spread to all reachable fresh oranges.

## 01 Matrix: Distance to the Nearest 0
In 01 Matrix, you are given a grid of 0s and 1s, and for every cell you must return the distance to the nearest 0.

Key insight: This is also a multi-source BFS problem, and the BFS must start from all 0 cells.

Why this works
Each 0 is already distance 0 from itself.
Its neighboring cells are distance 1, then their neighbors are distance 2, and so on.

That makes BFS a natural fit, because the first time a cell is reached, it is reached by the shortest path from some zero.

Queue contents
Each queue item stores:

(i, j, dist)
where dist is the distance from the nearest zero.

Initialization
Scan the whole grid
Push every 0 cell into the queue with distance 0
Mark those cells visited
Create:
an answer matrix
a visited matrix
BFS process
For each popped cell:

If it was already visited, skip it
Otherwise mark it visited
Write its distance into the answer matrix
Visit 4-direction neighbors
If a neighbor is inside bounds, not visited, and not 0, enqueue it with distance + 1
Key insight: The first time a cell is reached in this BFS is its shortest distance to any 0.

Important clarification
The source nodes depend on what distance you are measuring:

For 01 Matrix, you start BFS from all 0s
If a different problem asked for distance to the nearest 1, you would start from all 1s
Key insight: The BFS sources are determined by the value you want to measure distance from.

Common pitfalls
Starting from a single source instead of all zeros
Starting from the wrong value
Forgetting to check 4-direction movement only
Forgetting to skip already visited cells
Key takeaway: 01 Matrix is solved by seeding BFS with all zeros and expanding outward one layer at a time.

## Multi-Source BFS Pattern on Grids
Both Rotting Oranges and 01 Matrix use the same core pattern: multi-source BFS.

The recipe is:

Scan the grid
Add all source cells to the queue
Store the relevant state in each queue item:
coordinates
time or distance
BFS outward in 4 directions
Mark visited to avoid repeats
Use current + 1 for neighbors
Decide the final answer from the BFS frontier
Key insight: The queue carries the current layer, so each neighbor is exactly one step farther away.

A useful implementation rule was repeated: only enqueue a neighbor if it is:

inside the grid
not visited
valid for the problem’s source/target condition
Key takeaway: Multi-source BFS is the standard pattern whenever many starting points expand simultaneously and you need minimum time or minimum distance.

## Quick Reference
BFS queue rule: remove front, skip if visited, otherwise process, then enqueue unvisited neighbors
Graph BFS source: the starting node specified in the problem
Reachability: return True as soon as destination is popped/seen
Multiple BFS orders: possible due to neighbor ordering
Build graph from edges: for undirected graphs, add both u -> v and v -> u
Shortest path / minimum moves: BFS in unweighted graphs
Rotting Oranges: multi-source BFS from all rotten oranges, track maximum time, return -1 if fresh remain
01 Matrix: multi-source BFS from all zeros, assign each cell its first BFS distance
Queue entries on grids: usually (row, col, time/dist)
Always check: bounds + validity + not visited before enqueueing neighbors