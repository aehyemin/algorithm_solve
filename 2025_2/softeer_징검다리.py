import sys

input = sys.stdin.readline

n = int(input())
stone = list(map(int, input().split()))
dp = [1] * n

start = stone[0]
for i in range(1,n):
    for j in range(i):
        if stone[j]< stone[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))