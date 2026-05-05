class Solution:
   

    def exist(self, board: List[List[str]], word: str) -> bool:
        def visit(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            
            if board[row][col] != word[i]:
                return False

            temp = board[row][col] 
            board[row][col] = 'visited'
            res = (visit(row + 1, col, i + 1) 
                or visit(row - 1, col, i + 1) 
                or visit(row, col + 1, i + 1) 
                or visit(row, col - 1, i + 1))
            board[row][col] = temp
            return res


        for r in range(len(board)):
            for c in range(len(board[0])):
                if visit(r,c,0):return True
        return False
     


        