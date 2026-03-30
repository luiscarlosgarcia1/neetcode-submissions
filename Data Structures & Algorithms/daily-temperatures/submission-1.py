class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i,t))
                continue
                
            si, st = stack[-1]
            while t > st:
                res[si] = i - si
                stack.pop()
                if stack: 
                    si, st = stack[-1]
                else:
                    break
            
            stack.append((i,t))

        return res