class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a={}
        b={}

        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]]=i
            if t[i] not in b:
                b[t[i]]=i
            if a[s[i]]!=b[t[i]]:
                return False

        return True