from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        GRID = defaultdict(set)

        for r in range(9):
            for c in range(9):
                key = board[r][c]
                if key == '.':
                    continue
                if (key not in ROWS[r] or key not in COLS[c] or key not in GRID[r // 3][c // 3]):
                    return False
                ROWS[r].add(key)
                COLS[c].add(key)
                GRID[r//3][c//3].add(key)
        return True
        