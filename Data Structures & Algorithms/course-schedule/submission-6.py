class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref = defaultdict(list)
        for c, p in prerequisites:
            ref[c].append(p)

        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if ref[crs] == []:
                return True

            seen.add(crs)

            for p in ref[crs]:
                if not dfs(p):
                    return False

            seen.remove(crs)

            ref[crs] = []
            return True
            

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True