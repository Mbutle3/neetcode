from typing import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQUARE = defaultdict(set) 

        for r in range (9):
            for col in range (9):
                current_position = board[r][c]
                if current_position == '.':
                    continue
                if (current_position in ROWS[r] 
                or current_position in COLS[c] 
                or current_position in SQUARE[r // 3, c //3]):
                    return False
                ROWS[r].add(current_position)
                COLS[c].add(current_position)
                SQUARE[r // 3, c//3].add(current_position)
        return True
        
        