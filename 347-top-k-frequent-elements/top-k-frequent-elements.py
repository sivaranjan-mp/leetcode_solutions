class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        a={}
        nums.sort()
        for i in nums:
            if i not in a:
                a[i]=nums.count(i)
        num=dict(sorted(a.items(), key=lambda item: item[1], reverse=True))

        return list(num.keys())[:k]