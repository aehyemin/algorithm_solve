class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash = {}
        ans = 0
        max_ans = 0
        left = 0
        for i in range(len(nums)):
            while nums[i] in hash and hash[nums[i]] > 0:
                hash[nums[left]] -= 1
                ans -= nums[left]
                left += 1
            
            hash[nums[i]] = 1
            ans += nums[i]

            max_ans = max(max_ans, ans)
        return max_ans
​