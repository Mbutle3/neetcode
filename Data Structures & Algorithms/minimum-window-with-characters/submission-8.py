class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = {}
        have, need_count = 0, len(need)
        
        res = ""
        resLen = float("inf")
        l = 0

        for r in range(len(s)):
            # 1. Add s[r] to window
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # 2. Check if adding this char satisfied a need
            if char in need and window[char] == need[char]:
                have += 1

            # 3. Shrink from left while window is valid
            while have == need_count:
                # Update result
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                
                # Remove leftmost char and shrink
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return res