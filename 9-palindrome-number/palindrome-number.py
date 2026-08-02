class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        b=a[::-1]
        c = 121 if b.startswith("-") else 1

        if(a==b):
            return True
        elif(x==c):
            return True
        else:
            return False
