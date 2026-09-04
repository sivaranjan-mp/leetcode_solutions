class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split(" ")
        if len(a)!=len(pattern):
            return False
        b={}
        for i,j in zip(pattern, a):
            u=("i", i)
            v=("j", j)

            if u in b and b[u]!=j:
                return False
            if v in b and b[v]!=i:
                return False
            b[u]=j
            b[v]=i
        return True