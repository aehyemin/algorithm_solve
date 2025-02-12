class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        out = []
        for i in range(1, len(nums)):
            for j in range(i):
                ans = nums[i] + nums[j]  
                if target == ans:
                    out.append(j)  
                    out.append(i)  
        return out
    
