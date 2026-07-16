class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref = defaultdict(list)
        visited = set()

        for course, prereq in prerequisites:
            ref[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False
            if ref[course] == []:
                return True

            visited.add(course)

            for prereq in ref[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)

            ref[course] = []
            return True

        for course in range(len(prerequisites)):
            if not dfs(course):
                return False

        return True