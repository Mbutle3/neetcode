class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort the arr o(n * log(n))
        res = [] #create res arr to store output
        n = len(nums) # len of nums

        for i in range(n - 2): #gives us space to avoid runtime error since were going to have another loop 
            while i > 0 and nums[i] != nums[i - 1]: #ensure we're not checking the same val
                continue
            
            l = i + 1 #pointer 1 
            r = n - 1 #pointer 2

            while l < r: # two pointer approach - 1
                val = nums[i] + nums[l] + nums[r]
                if val < 0: 
                    l += 1 #move pointer 1 up
                elif val > 0:
                    r -= 1 #move pointer 2 down
                else:
                    res.append([nums[i], nums[l], nums[r]]) #appead all three vals into index 1 of the output arr
                    l += 1 #move pointer 1 up 
                    r -= 1 #move pointer 2 down
                    
                    while l < r and nums[l] == nums[l - 1]: #move pointer 1 until diff vals from one before - avoids duplicate checks
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: #move pointer 2 until diff vals from one before - avoids duplicate checks
                        r -= 1
        return res #return outpit arr


            



        