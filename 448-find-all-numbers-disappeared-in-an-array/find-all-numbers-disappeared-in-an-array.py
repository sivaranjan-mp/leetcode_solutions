class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=set(nums)
        a=[]
        for i in range(1, len(nums)+1):
            if i not in n:
                a.append(i)
        return a