class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #k개의 홀수 숫자가 있는 부분 배열
        cur = 0 #홀수의 개수를 저장
        dict = {0:1} #빈 구간의 홀수 개수가 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                cur += 1
            if cur - k in dict:
                ans += dict[cur-k]
            dict[cur] = dict.get(cur, 0) + 1
        return ans