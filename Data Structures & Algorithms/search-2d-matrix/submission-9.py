class Solution:
    
    def binarySearch(arr, target):
        L = 0
        R = len(arr) - 1
        mid = (L + R) // 2

        for i in range(len(arr)):
            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid - 1
            else:
                return True
        return -1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if (self.binarySearch(matrix[0])) == -1 and (self.binarySearch([matrix[1]]) == -1):
            return False
        return True
        