class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=sorted(nums1)
        b=sorted(nums2)
        i=0
        j=0
        r=[]
        while i<len(a) and j< len(b):
            if a[i]<b[j]:
                i+=1
            elif a[i]>b[j]:
                j+=1
            else:
                r.append(a[i])
                i+=1
                j+=1
        return r