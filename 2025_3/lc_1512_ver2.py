from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        ans = 0

        for i in nums:
            if i in hash:
                ans += hash[i]
                hash[i] += 1
            else:
                hash[i] = 1
        return ans
​