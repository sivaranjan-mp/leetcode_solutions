class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = {}

        for i in magazine:
            n[i] = n.get(i, 0) + 1
        for c in ransomNote:
            if c not in n or n[c] <= 0:
                return False
            n[c] -= 1
        
        return True