class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        startValue = 1
        ans = 0
           
        
        for i in range(len(nums)):
            ans += nums[i]
            if ans < 1: 
                startValue = max(1-ans, startValue)
                print(startValue)
            

        return startValue
        
