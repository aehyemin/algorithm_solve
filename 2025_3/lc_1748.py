class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        #한번만 사용된 숫자의 합
        has = {}
        ans = 0
        for i in nums:
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1
     
        for i, idx in has.items():
            if idx == 1:
                ans += i
        return ans     
​