

# https://www.geeksforgeeks.org/problems/topological-sort/1
from collections import deque
class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        # Code here
        graph = [[] for _ in range(V)]

        indegree = [0]*V

        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        q = deque()

        # Add all Element having Indegree = 0

        for i in range(V):
            if indegree[i]==0:
                q.append(i)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)

            for nbr in graph[node]:
                indegree[nbr]-=1
                if indegree[nbr]==0:
                    q.append(nbr)
        return ans

