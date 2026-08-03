class Solution(object):
    def isHappy(self, n):
        l=[]
        seen=set()
        while True:
            if(n<=4 and n!=1):
                r=False
                break
            elif(n==1):
                r=True
                break
            else:
                while True:
                    a=n%10
                    l.append(a)
                    n=n//10
                    if(n<=9):
                        l.append(n)
                        break
                    else:
                        continue

                b=len(l)
                sum=0

                for i in l:
                    sum+=(pow(i,2))

                if(sum==1):
                    r=True
                    break
                elif(sum in seen):
                    r=False
                    break

                else:
                    l[:] = []
                    n=sum
                    continue

                seen.add(sum)
        return r
        