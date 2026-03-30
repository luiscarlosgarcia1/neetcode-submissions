class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '([{':
                stack.append(c)
                continue
            elif c in ')]}':
                if len(stack) != 0 and table[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False