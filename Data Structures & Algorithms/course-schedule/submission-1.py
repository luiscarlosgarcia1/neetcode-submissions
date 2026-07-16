class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        ref = collections.defaultdict(list)
        visited = set()

        for i, j in pre:
            ref[i].append(j)

        def dfs(i):
            if i in visited:
                return False
            if ref[i] == []:
                return True

            visited.add(i)

            for j in ref[i]:
                if not dfs(j):
                    return False

            visited.remove(i)

            ref[i] = []
            return True

        for i, _ in pre:
            if not dfs(i):
                return False

        return True