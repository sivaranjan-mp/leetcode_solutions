class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        res1 = "".join(word1) 
        res2 = "".join(word2) 
        if(res1==res2):
            return True
        else:
            return False