class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        pre = 0
        mp = {0: 1}

        for num in nums:
            pre += num

            if pre - k in mp:
                c += mp[pre - k]

            mp[pre] = mp.get(pre, 0) + 1

        return c