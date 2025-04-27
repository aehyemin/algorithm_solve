class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        #(첫번째 + 세번째) / 2 = 두번째
        left = 0 
        cnt = 0
        for i in range(2, len(nums)):
            if 2*(nums[i-2] + nums[i]) == nums[i-1]:
                cnt += 1
        return cnt
