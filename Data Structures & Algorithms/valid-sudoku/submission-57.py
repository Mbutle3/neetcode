from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        GRID = defaultdict(set)
        
        for r in range (9):
            for c in range (9):
                
                val = board[r][c]

                if val == '.':
                    continue
                
                if val == ROWS[r]:
                    return False
                
                elif val == COLS[c]:
                    return False
                
                elif val in GRID[r // 3, c // 3]:
                    return False
                else:
                    ROWS[r].add(val)
                    COLS[c].add(val)
                    GRID[r // 3, c // 3].add(val)

        return True

