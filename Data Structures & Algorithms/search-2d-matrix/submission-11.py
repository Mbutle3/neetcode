class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #1. Find candidate row
        top = 0 
        bottom = ROWS - 1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                #target is in range of this row
                row = mid
                break
        else:
            return False
        

        #2. Binary Search Within That Row
        low = 0
        high = COLS - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[low][high]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
