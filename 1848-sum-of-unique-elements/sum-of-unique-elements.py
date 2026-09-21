class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        f = dict(Counter(nums))
        c = sum(key for key, val in f.items() if val == 1)
        return c