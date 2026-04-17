class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n 
        stack = []

        for idx, temp in enumerate (temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pop_idx = stack.pop()
                res[pop_idx] = i - idx
            stack.append(idx)
        return res
        