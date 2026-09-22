class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = {'(', '[', '{'}
        ref = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in opened:
                stack.append(c)
                continue

            if not stack:
                return False

            if ref[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return not bool(stack)