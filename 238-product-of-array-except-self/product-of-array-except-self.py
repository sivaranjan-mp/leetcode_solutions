class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p = 1
        z = 0
        
        for num in nums:
            if num == 0:
                z += 1
            else:
                p *= num
                
        result = []
        for num in nums:
            if z > 1:
                result.append(0)           
            elif z == 1:
                if num == 0:
                    result.append(p) 
                else:
                    result.append(0)             
            else:
                result.append(p // num) 
                
        return result