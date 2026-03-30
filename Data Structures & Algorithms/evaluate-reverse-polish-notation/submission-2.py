class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}

        for t in tokens:
            if t in operands:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(self.evaluate(n1, n2, t))
            else:
                stack.append(int(t))

        return stack[-1]

    def evaluate(self, num1, num2, op) -> int:
        if op == "+":
            return num2 + num1
        elif op == "-":
            return num2 - num1
        elif op == "*":
            return num2 * num1
        elif op == "/":
            return int(num2 / num1)
