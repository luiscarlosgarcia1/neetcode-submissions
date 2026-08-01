class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
        rank = [1] * len(edges)


        def find(i):
            res = i

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(i, j):
            pi, pj = find(i), find(j)

            if pi == pj:
                return 0

            if rank[pi] > rank[pj]:
                par[pj] = pi
                rank[pi] += rank[pj]
            else:
                par[pi] = pj
                rank[pj] += rank[pi]

            return 1
            

        for i, j in edges:
            if not union(i - 1, j - 1):
                return [i, j]         
        