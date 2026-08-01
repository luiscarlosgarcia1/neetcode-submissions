class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        

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
            
            if rank[pj] > rank[pi]:
                par[pi] = pj
                rank[pj] += rank[pi]
            else:
                par[pj] = pi
                rank[pi] += rank[pj]

            return 1


        res = n
        for i, j in edges:
            res -= union(i, j)

        return res