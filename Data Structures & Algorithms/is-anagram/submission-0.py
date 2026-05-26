class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for i in s:
            sDict[i] += 1
        for i in t:
            tDict[i] += 1
        return sDict == tDict