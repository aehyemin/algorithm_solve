import sys

input = sys.stdin.readline
a=2
n = int(input())
dp = [0] * (n+1)
dp[0] = 2
for i in range(1,n+1):
    dp[i] = dp[i-1] + 2**(i-1)

print(dp[n]**2)


#2, 3(2+1) , 5(4+1) ,9(8+1) ,  17(16+1)
#dp[1] = 3이 나와야 하고, dp = dp[i-1](2) + 2의0승
#start = 4 , 1 => 9 , 2 => 25
# 2의제곱  ,  3의제곱,  5의제곱,  8의제곱,  12의제곱??