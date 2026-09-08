class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c={}
        for i in t:
            c[i]=c.get(i,0)+1
        for i in s:
            c[i] -=1
            if c[i]==0:
                del c[i]
        return list(c.keys())[0]