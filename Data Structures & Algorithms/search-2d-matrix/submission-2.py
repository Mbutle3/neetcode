class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #get ROWS and COLS
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bottom_row = 0, ROWS - 1

        while top_row <= bottom_row:
            row = (top_row + bottom_row) // 2
            if target > matrix[row][-1]:
                top_row = row + 1
            elif target < matrix[row][0]:
                bottom_row = row - 1
            else:
                break
            
            if not (top_row <= bottom_row):
                return False
            
            row = (top_row + bottom_row) // 2

            left_pointer,right_pointer = 0, COLS - 1

            while left_pointer <= right_pointer:
                m = (left_pointer + right_pointer) // 2
                if target > target[row][m]:
                    left_pointer = m + 1
                elif target < target[row][m]:
                    right_pointer = m - 1
                else:
                    return True
            return False



            