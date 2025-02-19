class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
     #첫번째 섹션이 >= 두번째섹션 (합)   두번쨰는 1개이상의 요소
     total_sum = sum(nums) 
     ans = 0
     prefix = 0
     n = len(nums)
     for i in range(n-1):
        prefix += nums[i]
        if prefix >= total_sum-prefix:
            ans += 1
     return ans