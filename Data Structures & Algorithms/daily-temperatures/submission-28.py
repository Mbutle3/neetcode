class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp < temperatures[stack[-1]]:
                element_found_that_was_larger_index = stack.pop()
                res[element_found_that_was_larger_index] = i - element_found_that_was_larger_index
            stack.append(i)
        return res