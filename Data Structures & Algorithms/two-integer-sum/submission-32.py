class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #var to know how far to iterate 
        n = len(nums)

        #Creat a hashmap to value the values seen and their indexs 
        seen = {}

        #iterate though nums in from 0 .. n
        for i in range (n):
            compliment = target - nums[i] #create a var that is the value of target - current num
            if compliment in seen: #check if var is already in the hashmap
                return [seen[compliment], i] #if so return the index at that var and the current one
            else:
                seen[nums] = i #otherwise, add the [num, index] to the hashmap
        return [-1, -1] #if none of the checks pass return [-1,-1]


        