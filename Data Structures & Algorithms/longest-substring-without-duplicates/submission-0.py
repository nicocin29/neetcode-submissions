class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestStr = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in longestStr:
                longestStr.remove(s[l])
                l += 1
            longestStr.add(s[r])
            res = max(res, r - l + 1)
        return res