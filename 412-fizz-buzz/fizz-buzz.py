class Solution(object):
    def fizzBuzz(self, n):
        a=[]
        i=1
        for i in range(n+1):
            if(i!=0 and i%3==0 and i%5==0):
                a.append("FizzBuzz")

            elif(i!=0 and i%3==0):
                a.append("Fizz")

            elif(i!=0 and i%5==0):
                a.append("Buzz")

            elif(i!=0):
                a.append(str(i))
            else:
                pass

        return a