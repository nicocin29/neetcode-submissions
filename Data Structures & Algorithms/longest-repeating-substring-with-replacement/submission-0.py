class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        strStor = defaultdict(int)
        for r in range(len(s)):
            strStor[s[r]] += 1
            validWin = (r - l + 1) - max(strStor.values())
            if validWin <= k:
                res = max((r - l + 1), res)
            else:
                strStor[s[l]] -= 1
                l += 1
        return res
