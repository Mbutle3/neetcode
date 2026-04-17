class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n 
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pop_ele = stack.pop()
                res[pop_ele] = i - pop_ele
            stack.append(i)
        return stack


        