class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sets = set()
        ans = 0
        left = 0
        max_ans = 0
        for i in range(len(nums)):
            while nums[i] in sets:
                ans -= nums[left]
                sets.remove(nums[left])
                left += 1
                
            sets.add(nums[i])
            ans += nums[i]

            max_ans = max(max_ans, ans)
        return max_ans
​