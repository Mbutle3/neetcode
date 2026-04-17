from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bottom_row = 0, ROWS-1

        while top_row <= bottom_row:
            row = (top_row + bottom_row) // 2
            if target > matrix[row][-1]:
                top_row += 1
            elif target < matrix[row][0]:
                bottom_row -= 1
            else:
                left_pointer, right_pointer = 0, COLS - 1

                while left_pointer <= right_pointer:
                    m = (left_pointer + right_pointer) // 2
                    if target > matrix[row][m]:
                        left_pointer += 1
                    elif target < matrix[row][m]:
                        right_pointer -= 1
                    else:
                        return True
                return False
            return False




            
