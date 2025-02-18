class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<= 1:
            return 0
        left = 0
        cur = 1
        ans = 0
        for right in range(len(nums)):
            cur *= nums[right]

            while cur >= k and left<=right:
                cur //= nums[left]
                left += 1

            ans += right - left + 1
        return ans