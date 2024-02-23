class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'*','/','+','-'}
        print(int('-10'))
        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    res = operand1 + operand2
                elif token == '-':
                    res = operand1 - operand2
                elif token == '*':
                    res = operand1 * operand2
                elif token == '/':
                    if operand1 * operand2 < 0:
                        res = ceil(operand1 / operand2)
                    else:
                        res = floor(operand1 / operand2)
                stack.append(res)
            else:
                stack.append(int(token))
        # print(stack)
        return stack.pop()
