class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s= set(nums)
        l = 0
    
        for i in s:
            if i - 1 not in s:
                d = i
                c = 1
                while d + 1 in s:
                    d += 1
                    c += 1
            
                l = max(l, c)
            
        return l
        