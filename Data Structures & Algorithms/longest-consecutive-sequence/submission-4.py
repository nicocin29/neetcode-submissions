class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        stor = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) not in stor:
                length = 0
                while (num + length) in stor:
                    length += 1
                longest = max(length, longest)
        return longest                