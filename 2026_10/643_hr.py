class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum = window
        
        for right in range(k, len(nums)):
            window += nums[right] - nums[right-k]

            if window > max_sum:
                max_sum = window
        return max_sum / k

        
