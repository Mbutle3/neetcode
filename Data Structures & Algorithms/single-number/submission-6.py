class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seem.add(num)
        return list(seen)[0]

        