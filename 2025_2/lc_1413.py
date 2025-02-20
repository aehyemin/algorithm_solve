class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #더하는 과정에서 1보다 작으면 안됨 SUM >= 1
        startValue = 1
        ans = 0
        for i in nums:
            ans += i

            if ans < 1:
                startValue = max(startValue, 1 - ans)
            
        return startValue