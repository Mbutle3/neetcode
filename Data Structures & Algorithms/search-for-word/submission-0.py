class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        paths = []
        
        for r in range(len(board)):
            for c in range(len(board)[0]):
        
                ans = self.visit(row, col,0)
        return ans
        
    def visit(self, row, col, i):
        pos = board[row][col]

        if pos == word:
            return True
        if r > 0 or r > len(board) or c > 0 or c > len(board)[0]:
            return False
                
        visited[row][col] = True
        visit(row + 1, col, i + 1)
        visit(row - 1, col, i + 1)
        visit(row, col + 1, i + 1)
        visit(row, col - 1, i + 1)
        visited[row][col] = False
        


        