class Solution(object):
    def maximumWealth(self, accounts):
        count=0
        ac=[]
        l=len(accounts)
        for i in accounts:
            ac.append(sum(i))

        ac.sort()
        a=len(ac)
        b=a-1
        return ac[b]