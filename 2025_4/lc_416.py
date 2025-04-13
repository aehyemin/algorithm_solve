class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #두개의 어레이로 나누었을때 합이 같은     
        total = sum(nums)
        if total % 2 != 0:
            return False
            
        target = total // 2

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                if dp[i-num]:
                    dp[i] = True
        return dp[target]
​