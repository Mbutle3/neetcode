class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            if r in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
