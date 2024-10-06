import sys
input= sys.stdin.readline
T = int(input())

for i in range(T):
    N = int(input()) #N가지 동전
    coins = map(int, input().split())
    M = int(input()) #만들금액M
#동전의 개수를 세는게 아니고 방법의 개수   
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1,M+1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[M])
        
    