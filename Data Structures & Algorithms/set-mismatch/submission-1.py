class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        first = None

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                first = num
        

        second = None
        for i in range(1, len(nums) + 1):
            if i not in s:
                second = i
        
        return [first, second]
        