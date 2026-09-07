class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for i in s:
            f[i]=1+f.get(i,0)
        for i,j in enumerate(s):
            if f[j]==1:
                return i
        return -1