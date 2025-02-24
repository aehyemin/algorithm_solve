class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #타겟이랑 같거나 큰 minimal length subarray

        left = 0
        score = 0
        length = 10000000

        for i in range(len(nums)):
            score += nums[i]

            while score >= target:
                length = min(length, i - left + 1)
                score -= nums[left]
                left += 1
            
        return length if length != 10000000 else 0