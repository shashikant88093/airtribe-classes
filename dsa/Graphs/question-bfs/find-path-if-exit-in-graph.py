# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

# Input: 
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

from collections import deque
# Input: 
# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

def bfs(n,edges,src,destination):
    graphs = [[] for _ in range(n)]
    print(graphs)

    for u,v in edges:
        graphs[u].append(v)
        graphs[v].append(u)


    print(graphs)

    vis = [False] * n

    q = deque()
    q.append(source)

    while len(q) >0:
        fnt = q.popleft()
        if fnt == destination:
            return True
        if vis[fnt] == True:
            continue
        vis[fnt] = True

        for nbr in graphs[fnt]:
            if vis[nbr] == False:
                q.append(nbr)
    return False








print(bfs(n,edges,source,destination))
