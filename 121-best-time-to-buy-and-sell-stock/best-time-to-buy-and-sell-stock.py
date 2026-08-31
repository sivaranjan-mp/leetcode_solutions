class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        p=0
        for i in prices[1:]:
            if a>i:
                a=i
            p=max(p,i-a)
        return p