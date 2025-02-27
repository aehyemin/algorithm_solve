class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avg = [-1]*n
        slide = 2*k + 1
        slide_sum = sum(nums[:slide])

        if slide > n:
            return avg

        for i in range(k, n-k):
            avg[i] = slide_sum // slide
            if i + k + 1 < n:
                slide_sum += nums[i+k+1]
                slide_sum -= nums[i-k]

        return avg
       