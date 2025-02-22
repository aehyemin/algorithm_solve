class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #바이크 0에서 시작
        n = len(gain)
        prefix = [0]*(n+1)

        score = 0
        for i in range(1, n+1):
            score += gain[i-1]
            prefix[i] = score

        return max(prefix)