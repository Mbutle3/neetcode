class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        maxLen = 0
        l = 0
        n = len(s)

        for r in range(n):
            while r in st:
                st.remove(s[l])
                l += 1
            else:
                st.add(s[r])
                maxLen = max(maxLen, r - l + 1)
        return maxLen
