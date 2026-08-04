class Solution(object):
    def singleNumber(self, nums):
        a=[]
        num=nums
        b=len(nums)
        if (b==1):
            return nums[0]
        for x in nums:
            if nums.count(x) > 1:
                a.append(x)

                
        for i in range(b):
            if(num[i] not in a):
                return nums[i]