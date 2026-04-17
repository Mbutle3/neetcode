class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Empty Cases
        if not matrix or not matrix[0]:
            return False
        
        # Get # of Rows and Cols
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #1st Pass Binary Search To Find Row
        top = 0
        bottom = ROWS - 1
        row = 0

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][0]:
                top = mid + 1
            elif target < matrix[mid][-1]:
                bottom = mid - 1
            else:
                row = mid
        else:
            return False

        #2nd Pass Binary Search To Find Val In Chosen Row
        left = 0 
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[row][mid]

            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return True
        return False

        