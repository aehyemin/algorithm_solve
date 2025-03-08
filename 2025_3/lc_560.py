class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        ans = 0
        dict = {0:1} # 각 누적합이 몇번 등장했는
        #아무 원소도 포함하지 않은 누적합은 0 
        n = len(nums)

        for i in range(n):
            cur += nums[i]
            if cur - k in dict:
                ans += dict[cur-k]
            dict[cur] = dict.get(cur, 0) + 1
        return ans

        #1. 누적합을 구한다
        #2. 누적합이 몇번 등장했는지 저장 
        #3. 부분배열 개수세기 
        #4. 해시맵 업데이트

        #부분 배열의 합이 k인 구간
        #cur - cur_j = k
        #cur - (cur-k) = k