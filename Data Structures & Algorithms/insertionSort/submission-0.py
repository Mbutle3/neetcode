# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                j -= 1
        return arr
        