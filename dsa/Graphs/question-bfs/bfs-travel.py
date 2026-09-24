# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from collections import deque
adj =[[2, 3, 1], [0], [0, 4], [0], [2]]


def bfs(adjencent):

    vis = [False] * len(adjencent)

    q = deque()

    q.append(0)

    ans = []

    while len(q) >0:
        fnt = q.popleft()

        if vis[fnt] == True:
            continue
        vis[fnt] = True
        ans.append(fnt)

        for nbr in adj[fnt]:
            if vis[nbr] == False:
                q.append(nbr)
    return ans




print(bfs(adj))