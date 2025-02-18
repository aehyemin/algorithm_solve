class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i-k]
            max_sum = max(max_sum, cur)
        return max_sum / k