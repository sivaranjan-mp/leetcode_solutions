class Solution(object):
    def addDigits(self, num):
        sum=0
        while True:
            a=num%10
            b=num/10
            sum=a+b
            if(sum>=1 and sum<=9):
                return sum
                break
            elif(sum==0):
                return sum
                break
            else:
                num=sum