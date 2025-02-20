class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #더하는 과정에서 1보다 작으면 안됨 SUM >= 1
        start = ans = 0

        for num in nums:
            ans += num
            start = min(ans, start)

        return 1 - start   