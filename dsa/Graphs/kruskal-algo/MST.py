# https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1

from typing import List

class Solution:
    
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        par = [i for i in range(V)]
        rank = [1]*V
        
        def find(a):
            if par[a]!=a:
                par[a]=find(par[a])
            return par[a]
        def find(a):
            if par[a]==a:
                return a
            else:
                par[a]=find(par[a])
            
            
        # def merge(a,b)
        def union(a,b):
            par_a = find(a)
            par_b = find(b)
            
            if rank[par_a]<rank[par_b]:
                par[par_a]=par_b
            elif rank[par_a]>rank[par_b]:
                par[par_b]=par_a
            else:
                par[par_b]=par_a
                rank[par_a]+=1
                
        edges.sort(key=lambda x:x[2])
        
        cost = 0
        for u,v,w in edges:
            pu = find(u)
            pv = find(v)
            if pu == pv:
                continue
            else:
                union(u,v)
                cost+=w
        
        return cost
                    
        
        
        