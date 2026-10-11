class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        right = len(nums) - 1
        while left < right:
            if k > nums[left] + nums[right]:
                left += 1
            elif k < nums[left] + nums[right]:
                right -= 1
            else:
                ans += 1
                left += 1
                right -= 1
        return ans
            
               
                
