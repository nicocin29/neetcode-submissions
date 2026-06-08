class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                comp = 0 - nums[i] - nums[j]
                if comp in nums[j+1:]:
                    to_add = sorted([nums[i], nums[j], comp])
                    if to_add not in res:
                        res.append(to_add)
                j += 1
        return res
