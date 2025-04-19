class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countPair(nums, upper) - self.countPair(nums, lower - 1)
    def countPair(self, nums:List[int], target:int) -> int:
        cnt = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                cnt += right - left
                left += 1
        return cnt