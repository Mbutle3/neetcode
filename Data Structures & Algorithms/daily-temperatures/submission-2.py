class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        left = 0
        larger_val = temperatures[0]
        res = []
        counter = 0
        n = len(temperatures)


        for right in range(1, n):
            right_val = temperatures[right]
            counter = 1
            while left < right and right_val < larger_val :
                counter += 1
            res.append(counter)
            left = right
        return res

        