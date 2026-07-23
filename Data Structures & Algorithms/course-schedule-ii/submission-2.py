class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        ref = defaultdict(list)
        visited, cycle = set(), set()

        for crs, pre in prerequisites:
            ref[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)

            for pre in ref[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res