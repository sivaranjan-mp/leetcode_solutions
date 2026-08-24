class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        a=Counter(nums)
        return [item[0] for item in a.most_common(k)]