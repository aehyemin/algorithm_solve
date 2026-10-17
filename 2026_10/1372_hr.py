class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix = 0
        max_one = prefix
        for i in range(len(gain)):
            prefix += gain[i]
            max_one = max(prefix, max_one)
        
        return max_one
            
