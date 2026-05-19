class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set() #declaring set to keep track of chars we encounter
        l = 0  # left pointer to build substring width
        longest = 0  #longest substring found

        for r in range(len(s)): #use r as runner to check through the string
            while s[r] in seen: #while we already encounter a char 
                seen.remove(s[l]) #remove the prev seen char from the set **s[l] is always behind s[r]** 
                l += 1 # move the l pointer up by one
            seen.add(s[r]) #otherwise, add the current char to the set and let the for loop continue
            longest = max(longest, r - l + 1) #take the max between the current longest and the current window width (r - l + 1)
        return longest #return the longest var 


