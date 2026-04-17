class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if substr empty just return ""
        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("inf")
        left = 0 
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            #does this count satisfy what were are looking for?
            if c in countT and window[c] == countT:
                have += 1
            
            while have == need:
                #update our result
                #calc size of curr window
                if (right - left + 1) < resLen:
                    res  = [left, right]
                    resLen = right - left + 1
                #pop from left of our window
                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left : right + 1]
                


        