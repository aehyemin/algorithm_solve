class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        #가장 많은 빈도수의 합 반환토탈 프리퀀시를 반환하라
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1
       
        freq = max(hash.values())

        ans = 0
        for num, idx in hash.items():
            if idx == freq:
                ans += freq
        return ans