class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, temp in enumerate(temperatures):
            if stack and temp > stack[-1]:
                stack.pop()
            stack.append(temp)
            res.append(i)
        return res