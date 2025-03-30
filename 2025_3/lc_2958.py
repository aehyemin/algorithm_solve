class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hash = {}
        max_len = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] not in hash:
                hash[nums[right]] = 1
            else:
                hash[nums[right]] += 1

            while hash[nums[right]] > k:
                hash[nums[left]] -= 1
                if hash[nums[left]] == 0:
                    del hash[nums[left]]
                left += 1
          
            max_len = max(max_len, right - left + 1)

        return max_len