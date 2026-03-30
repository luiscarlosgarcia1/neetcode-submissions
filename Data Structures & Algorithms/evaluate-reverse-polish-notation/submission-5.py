class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+": lambda n1, n2: n1 + n2,
                    "-": lambda n1, n2: n1 - n2,
                    "*": lambda n1, n2: n1 * n2,
                    "/": lambda n1, n2: int(n1 / n2),}

        for t in tokens:
            if t in operands:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(operands[t](n2, n1))
            else:
                stack.append(int(t))

        return stack[-1]