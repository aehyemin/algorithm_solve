class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #한번 순회하면서 prefix sum
        #앞에부터 더함, 슬라이딩 윈도우
        prefix = 0
        left = 0
        min_val = float('inf')
        for i in range(len(nums)):
            prefix += nums[i]
        #2+3+1+2, 4 -> 4 | 4+3
            while prefix >= target:
                prefix -= nums[left]
                min_val = min(min_val, i+1-left)
                left += 1
        if min_val == float('inf'):
            return 0
        else:
            return min_val
            
