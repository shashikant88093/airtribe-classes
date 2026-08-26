## 3 Steps to Solve Recursion Problems

1. **Identify the Base Case**: Determine the simplest instance of the problem, which can be solved directly without further recursion. This is crucial to prevent infinite recursion.

2. **Break Down the Problem**: Divide the problem into smaller subproblems that resemble the original problem. This often involves reducing the size of the input or changing the state in a way that brings it closer to the base case.

3. **Combine Results**: Once the base case is reached and the subproblems are solved, combine the results to form the solution to the original problem. This may involve aggregating values, reconstructing data structures, or applying additional logic.



## From mentor

The session also emphasized why DSA matters beyond interview prep: it is fundamentally about problem-solving, and that helps in real company and product work too. A short graph-algorithm aside mentioned the standard toolkit you should know: DFS, BFS, Bellman-Ford, and Dijkstra’s algorithm.

How to think about recursive execution
A call chain behaves like a stack of pending work:

main calls F2
F2 calls F3
F3 calls F1
then execution unwinds in reverse order
This is why recursive programs often feel like they “pause” at the recursive call and resume later.

Key insight: A function is only done after all the lines below the recursive call are completed.

The 3-step method for recursion problems
A reusable framework was given for solving recursion questions:

Understand the requirement
Have faith in the recursion
Relate the current problem to the smaller subproblem
“Faith in recursion” means you do not solve the smaller call again yourself; you trust it to work and focus on how to use its answer.

Key takeaway: Recursion becomes manageable when you clearly separate the current step, the smaller subproblem, and the base case.

