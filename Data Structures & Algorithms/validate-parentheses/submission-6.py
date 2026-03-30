class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = set({'(', '[', '{'})

        ref = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in opened:
                stack.append(c)
            elif stack and stack[len(stack)-1] == ref[c]:
                stack.pop()
            else: return False

        return False if stack else True