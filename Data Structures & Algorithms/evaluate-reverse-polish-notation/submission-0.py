class Solution:
    def evalRPN(self, tokens: List[str]) -> int:




        """
        1 -> 2 - > + 
            (1 + 2)
        3 -> *
            ( (1 + 2) * 3 )
        4 -> -
            ( ( (1 + 2) * 3 ) - 4) = 5    

        when we encounter an operand add to the stack 
        when we encounter an operand add a () to the stack 
        
        """

        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(char))
        return stack[0]



        