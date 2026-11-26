class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for token in tokens:
            if token == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif token == "-":
                subval2 = stack.pop()
                subval1 = stack.pop()
                val = subval1 - subval2
                stack.append(val)
            elif token == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif token == "/":
                subval2 = stack.pop()
                subval1 = stack.pop()
                val = int(float(subval1) / subval2)
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[0]
        

        