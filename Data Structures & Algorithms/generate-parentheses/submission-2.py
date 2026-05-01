class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openings, closings):
            if openings == closings == n:
                res.append("".join(stack))
                return

            if openings < n:
                stack.append("(")
                backtrack(openings + 1, closings)
                stack.pop()
        
            if closings < n:
                stack.append(")")
                backtrack(openings, closings + 1)
                stack.pop()
        backtrack(0,0)
        return res