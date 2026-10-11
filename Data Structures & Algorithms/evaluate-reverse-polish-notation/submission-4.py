import math
from collections import deque

class Solution:
    def evalOperation(self, operandA, operandB, operation) -> int:
        match operation:
            case "+":
                return int(operandA) + int(operandB)
            case "-":
                return int(operandA) - int(operandB)
            case "*":
                return int(operandA) * int(operandB)
            case "/":
                return math.trunc(int(operandA) / int(operandB))

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                operandB = stack.pop()
                operandA = stack.pop()
                stack.append(self.evalOperation(operandA, operandB, tokens[i]))
            else:
                stack.append(tokens[i])

        return int(stack.pop())