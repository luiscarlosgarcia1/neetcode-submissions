class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = {'(', '[', '{'}
        ref = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in opened:
                stack.append(c)
                continue

            if not stack or ref[c] != stack[-1]:
                return False

            stack.pop()

        return not bool(stack)