class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums)-1:
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return list([i,j])
            i += 1