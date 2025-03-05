class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for i in range(n+1):
            dict[i] = 0
 
        for char in nums:
            if char in dict:
                dict[char] += 1
  
        for i in range(n+1):
            if dict[i] == 0:
                return i