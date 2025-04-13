class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #good number count: 짝수 인덱스는 짝수, 홀수 인덱스는 홀수이며 소수 1,3,5,7

        ans = 1
        MOD = 10**9 + 7
        #짝수, 홀수, 짝수, 홀수, 짝수
        if n % 2 == 0: #짝수
            a = n // 2 
            # ans = (5**a) * (4**a)
            ans = pow(5, a, MOD) * pow(4,a, MOD)
        else: #홀수
            a = n // 2 + 1 #3
            # ans = (5**a) * (4**(n//2))
            ans = pow(5, a, MOD) * pow(4, n//2, MOD)

        return ans % (10**9 + 7)