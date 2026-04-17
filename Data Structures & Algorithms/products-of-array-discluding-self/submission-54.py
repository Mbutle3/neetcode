class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix = 1
        for i in range (len(nums)):
            nums[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range (nums - 1, -1, -1):
            postfix *= nums[i]
            nums[i] = postfix
        

        