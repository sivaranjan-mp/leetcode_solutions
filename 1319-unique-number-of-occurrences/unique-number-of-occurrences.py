class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr.sort()
        a=[]
        i=0
        while i<len(arr):
            b=1
            while i+1<len(arr) and arr[i] == arr[i+1]:
                b+=1
                i+=1
            a.append(b)
            i+=1
        a.sort()
        for j in range(1, len(a)):
            if(a[j]==a[j-1]):
                return False
        return True