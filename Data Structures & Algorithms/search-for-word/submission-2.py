class Solution:
   

    def exist(self, board: List[List[str]], word: str) -> bool:
        def visit(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row > len(board) or col < 0 or col > len(board[0]):
                return False
                    
            board[row][col] = True
            res = (visit(row + 1, col, i + 1) 
                or visit(row - 1, col, i + 1) 
                or visit(row, col + 1, i + 1) 
                or visit(row, col - 1, i + 1))
            board[row][col] = False
            return res


        ans = False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                ans = visit(r, c,0)
        return ans
     


        