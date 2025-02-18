class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k <= 1:
            return max(nums)
        left = 0
        ans = - 100000
        cur = 0
        for right in range(len(nums)):
            cur += nums[right]
            if right - left + 1 == k:
                ans = max(ans, float(cur / k))
                cur -= nums[left]
                left += 1
        return ans 