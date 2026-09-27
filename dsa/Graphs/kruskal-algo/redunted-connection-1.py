# https://leetcode.com/problems/redundant-connection/description/

class Solution:
    def find(self,a):
        if self.par[a]==a:
            return a
        else:
            self.par[a]=self.find(self.par[a])
            return self.par[a]a

    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)

        if self.rank[pa]> self.rank[pb]:
            self.par[pb]=pa
        elif self.rank[pb]>self.rank[pa]:
            self.par[pa]=pb
        else:
            self.par[pa]=pb
            self.rank[pb]+=1
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        self.par = [0]* (len(edges)+1)
        self.rank = [0]* (len(edges)+1)

        for i in range(len(self.rank)):
            self.par[i]=i
            self.rank[i]=1
        
    
        for e in edges:
            src = e[0]
            dest = e[1]

            ps = self.find(src)
            pd = self.find(dest)

            if ps == pd:
                return e
            else:
                self.union(src,dest)
        return [0,0]
                
        