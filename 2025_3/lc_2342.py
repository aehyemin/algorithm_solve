class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        #숫자 자리수의 합이 같은 인덱스
        num = {}
        max_len = -1
        
        for i in nums:
            original = i
            ans = 0

            while i>0:
                ans += i % 10
                i //= 10
            if ans not in num:
                num[ans] = []
            num[ans].append(original)

        for k, idx in num.items():
            if len(idx) >= 2:
                idx.sort()
                max_len = max(max_len, idx[-1]+idx[-2])

        return max_len
