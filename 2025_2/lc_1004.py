class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = 0 #0카운트
        left = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans