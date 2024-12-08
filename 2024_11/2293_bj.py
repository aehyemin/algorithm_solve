n, k = map(int, input().split())
#n가지 종류의 동전, 목표 k원
coin = []
for _ in range(n):
    coin.append(int(input()))
dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for j in range(c,k+1):
        dp[j] += dp[j-c]
#x원을 만들 수 있는 경우의 수
#보류
print(dp[k])