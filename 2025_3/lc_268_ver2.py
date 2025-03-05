class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = set(nums)
        n = len(nums)
        new_num = set(range(n+1))
        return (new_num - num).pop()