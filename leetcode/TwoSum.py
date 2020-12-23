class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = []
        for i in range(0,len(nums)):
            c = target - nums[i]
            if c in nums:
                for j in range(i+1,len(nums)):
                    if c == nums[j]:
                        return([i,j])
    