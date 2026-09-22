# Complete Kid-Friendly Guide to Graphs & DFS 🎈

Here is every single concept, rule, code snippet, and problem from the class notes, explained simply without any links.

---

## 1. Classroom Resources Mentioned 🎒

During class, the instructor and peers shared several materials:
* **Meeting Transcripts:** Notes and transcriptions taken via Tactiq (shared by Prasad Shelar and Pratima Dabhi).
* **Practice Missions:**
  * **Number of Provinces:** A puzzle about counting connected friend groups (shared by Himanshu).
  * **Depth-First Traversal for a Graph:** A practice maze to explore every path in a graph (shared by Himanshu).
  * **Number of Distinct Islands:** A grid puzzle about finding unique island shapes (shared by Himanshu).
* **Feedback Form:** A class feedback check-in (shared by Mohit from Airtribe).

---

## 2. What is a Graph? (The Playground Map) 🗺️

A graph is simply **things** and the **connections between them**.

* **Nodes (or Vertices):** The items themselves. Think of them as **kids standing on a playground**.
* **Edges:** The lines connecting them. Think of them as **two kids holding hands** or a piece of string tied between them.

---

## 3. The Different Kinds of Graphs 🏷️

Graphs come in different styles, just like playground games:

### Directed vs. Undirected
* **Undirected Graph (Two-Way Street):** A friendly handshake. If Kid A holds hands with Kid B, Kid B is also holding hands with Kid A. You can walk back and forth freely.
* **Directed Graph (One-Way Slide):** Like a water slide! An arrow points from $1 \rightarrow 2$. You can slide down from 1 to 2, but you cannot climb backwards from 2 to 1. Direction matters!

### Cyclic vs. Acyclic
* **Cyclic (Ring-Around-the-Rosy):** There is a closed loop. If you start at Kid 1, walk to Kid 2, then Kid 3, you can loop right back to Kid 1 ($1 \rightarrow 2 \rightarrow 3 \rightarrow 1$).
* **Acyclic (No Loops):** A straight line or a star. You can never walk in a complete circle.

### Weighted vs. Unweighted
* **Weighted Graph (Toll Bridges):** Connections carry a measurable value (like "costs $5", "takes 10 minutes", or "distance of 3 miles"). These matter when calculating the cheapest or shortest path (such as Dijkstra's algorithm).
* **Unweighted Graph:** Every bridge is equal. Crossing any edge simply counts as 1 step.

### Connected vs. Disconnected
* **Connected Graph:** One big whole! Every kid can reach every other kid by following the handshakes.
* **Disconnected Graph:** The kids are split into separate groups (like three kids playing tag in one corner and two kids playing in the sandbox far away).

### Tree vs. Graph 🌳
* A **Tree** is just a well-behaved graph:
  1. It has **no loops** (acyclic).
  2. It is **connected** in one single piece.
  3. If there are $V$ kids, it has exactly $V - 1$ handshakes.
* **Golden Rule:** Every tree is a graph, but not every graph is a tree!

### Degrees & Components
* **For Directed Graphs:**
  * **In-degree:** How many arrows point **into** you (incoming connections).
  * **Out-degree:** How many arrows point **away** from you (outgoing connections).
  * **Total Degree:** $\text{In-degree} + \text{Out-degree}$.
* **For Undirected Graphs:**
  * **Degree:** The total number of adjacent friends you are holding hands with.
* **Component:** A group of connected kids. A single lonely kid standing by themselves still counts as a 1-person component!

---

## 4. Storing Graphs in a Computer's Brain 💾

Computers cannot draw visual maps, so they store graphs using one of two methods:

### Method A: Adjacency Matrix (The Big Attendance Grid)
A giant square grid table where every kid is listed on the rows and the columns:
* Put a **1** if two kids share an edge.
* Put a **0** if they do not.
* For an undirected graph, the table is symmetric (a mirror reflection across the diagonal).
* A self-loop (a kid connected to themselves) sits on the main diagonal (like `matrix[0][0]`).

* **Advantage:** Checking if two kids are friends is instant ($O(1)$ time).
* **Limitation:** It takes up $O(V^2)$ memory space. For sparse graphs where few connections exist, it wastes vast amounts of storage on zeros.

### Method B: Adjacency List (The Pocket Address Book)
Each kid simply keeps a mini list of their immediate neighbors:
* Kid 0: `[1]`
* Kid 1: `[0, 2]`
* Kid 2: `[1]`
* Kid 3: `[]` *(alone)*
* Kid 4: `[5]`
* Kid 5: `[4]`

* **Advantage:** Highly space-efficient ($O(V + E)$). It only stores actual connections, making it the practical choice for most programs.
* **Limitation:** Checking if two kids are connected can take slightly longer because you have to read through a neighbor list.
* **Weighted Graphs:** Instead of storing just neighbor IDs, store an `Edge` object containing the starting point ($u$), destination ($v$), and weight ($w$), structured like `List[List[Edge]]`.

---

## 5. DFS: The Maze Explorer! (Depth-First Search) 🏃‍♂️

DFS explores like walking a hedge maze: **walk as far forward as possible along one hallway, and when blocked, backtrack to the last turn!**

### The Core Pattern
1. **Chalk Mark (`visited[node] = True`):** Mark yourself so you do not visit the same spot twice and get trapped in an endless loop.
2. **Recursive Step:** Look at every neighbor; if they are unvisited, run down that hallway immediately.
3. **Backtrack:** When all neighbors are done, return to the junction behind you.

```python
def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)