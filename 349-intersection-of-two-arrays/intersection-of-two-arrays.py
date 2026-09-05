class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a={}
        for i in nums1:
            a[i]=a.get(i,0)+1
        r=[]
        for i in nums2:
            if i in a:
                r.append(i)
                del a[i]
        return r
        