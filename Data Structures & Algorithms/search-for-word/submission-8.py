class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, i):
            if row < 0 or row >= len(word) or col < 0 or row >= len(word):
                return False

            if board[row][col] != word[i]:
                return False
            
            if i == len(word):
                return True
            
            res = (
                backtrack(row + 1, col, i + 1) or 
                backtrack(row - 1, col, i + 1) or 
                backtrack(row, col + 1, i + 1) or 
                backtrack(row, col - 1, i + 1)
            )

            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True
        return False
            
