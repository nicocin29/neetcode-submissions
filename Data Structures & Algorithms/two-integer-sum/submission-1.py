class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevDict:
                return [prevDict[diff], i]
            prevDict[num] = i
        

        
        
      #  i = 0
      #  while i < len(nums)-1:
      #      for j in range(len(nums)):
       #         if i != j:
       #             if nums[i] + nums[j] == target:
        #                return list([i,j])
       #     i += 1