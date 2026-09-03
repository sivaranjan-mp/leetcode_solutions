class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r=len(nums)
        for i in range(len(nums)):
            r+=i-nums[i]
        return r
        