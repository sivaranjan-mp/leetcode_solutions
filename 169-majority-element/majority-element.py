class Solution(object):
    def majorityElement(self, nums):
        n = {}

        for i in nums:
            n[i] = n.get(i, 0) + 1

        return max(n, key=n.get)