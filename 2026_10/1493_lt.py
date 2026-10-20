class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero = 0 #0의 개수
        window = 0
        k = 0 #left위치
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1

            while zero > 1: 
                if nums[k] == 0:
                    zero -= 1
                k += 1
            
            window = max(window, i-k)
        return window
