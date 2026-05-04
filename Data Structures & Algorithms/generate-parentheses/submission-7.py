class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(parentheses, openN, closedN):
            if openN == closedN == n:
                res.append("".join(parentheses))
            
            if openN < n:
                parentheses.append('(')
                backtrack(parentheses, openN + 1, closedN)
                parentheses.pop()

            if closedN < openN:
                parentheses.append(')')
                backtrack(parentheses, openN, closedN + 1)
                parentheses.pop()
            
        backtrack([],0,0)
        return res