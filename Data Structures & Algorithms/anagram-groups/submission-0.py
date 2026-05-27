class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = defaultdict(list)
        for n in strs:
            sortedStrs["".join(sorted(n))].append(n)
        return list(sortedStrs.values())