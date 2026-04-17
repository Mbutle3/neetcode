class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #handle edge case of empty matrix
        if not matrix or not matrix[0]:
            return False
        
        #Store length of # of Rows and Cols 
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #1st pass Bin Search To Find Row
        top = 0
        bottom = ROWS - 1
        row = 0

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][-1] > target:
                bottom = mid - 1
            else:
                row = mid
                break
        else:
            return False

        #2nd pass Bin Search To Find Val In Row
        left = 0
        right = COLS - 1
        
        while left <= right:
            mid = (left + right) // 2
            val = matrix[row][mid]

            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True
        return False
        