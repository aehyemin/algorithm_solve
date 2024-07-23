#물건의 무게 > 배낭의 무게
# 전꺼

#물건의 무게 <= 배낭의 무게
# dp[K+1][W]= K+1가치 + dp[k][w-m]

#N물품의 수, K버틸수있는 무게
N, K = map(int,input.split())
items = []
for _ in range(N):
    W, V = map(int,input().split())
    items.append((W, V))
    
# 배낭 무게의 가치를 저장한다
#배낭의 최대 무게가 K이므로 dp배열의 크기는 K+1이 되어야 0부터k까지
# 모든 경우를 포함할 수 있다.
#배낭의 무게에 따라 설정하는 것이 더 효율적
#dp[j] j무게 이하로 담을수있는 최대가치
dp = [] * (K+1)

#역순으로 계산하는것은 배낭의 최대 무게에서 최소 무게까지 역순으로 배열 업데이트
for item in items:
    W, V = item
    for k in range(K,W-1,-1):
        dp[k] = max(dp[k], dp[k-W]+V)
print(dp[-1])


