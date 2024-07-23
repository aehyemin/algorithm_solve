import sys
input = sys.stdin.readline
#물품의 수, 버틸수있는무게K
N, K = map(int,input().split())
items = []
for i in range(N):
    W, V = map(int, input().split())
    items.append((W, V))
    
dp = [0] * (K+1)
#W각 물건의 무게, V물건의 가치
for item in items:
    W, V = item
    for j in range(K, W-1, -1):
        dp[j] = max(dp[j], dp[j-W]+V)
print(dp[-1])
        