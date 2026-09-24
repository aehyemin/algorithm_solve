class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            l = str(nums[i])
            ans = 0
            for j in range(len(l)):
                ans += int(l[j])
            if ans == i:
                return i
        return -1

            
