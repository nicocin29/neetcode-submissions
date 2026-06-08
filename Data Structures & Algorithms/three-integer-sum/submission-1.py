class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                comp = 0 - nums[i] - nums[j]
                if comp in nums[j+1:]:
                    if [nums[i], nums[j], comp] not in res:
                        res.append([nums[i], nums[j], comp])
                j += 1
        return res
