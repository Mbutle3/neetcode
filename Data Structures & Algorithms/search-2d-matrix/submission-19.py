class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            
            if matrix[top][mid] < target:
                top = mid + 1
            elif matrix[mid][bottom] > target:
                bottom = mid - 1
            else:
                row = mid
        else:
            return False

        top = 0
        bottom = COLS - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            val = [row][mid]

            if val < target:
                top = mid + 1
            elif val > target:
                bottom = mid - 1
            else:
                return True
        return False
        