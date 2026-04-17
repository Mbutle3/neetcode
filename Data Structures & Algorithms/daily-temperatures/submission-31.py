class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        
        for idx, temp in enumerate(temperatures):
            while idx < n and temp > temperatures[stack[-1]]:
                pop_idx = stack.pop()
                res[stack[-1]] = idx - pop_idx
            stack.append(idx)
        return res