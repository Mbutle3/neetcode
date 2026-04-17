class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #Empty Case
        if not matrix or len(matrix) == 0:
            return False

        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1
        row = 0

        while top <= bot:
            mid = (top + bot) // 2

            if target > matrix[mid][0]:
                top = mid + 1
            elif target < matrix[mid][-1]:
                bot = mid - 1
            else:
                row = mid
                break
        
        left = 0
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[row][mid]
            if target == val:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False

        