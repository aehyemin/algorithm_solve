import sys

input = sys.stdin.readline
n, k = map(int, input().split())
#물품의 수, 버티는무게
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
    #무게, 가치
dp = [[0]*(k+1) for i in range(n+1)]
print(lst)
 #배낭의 허용 무게보다 크면 넣지 않는다
 # 현재배낭에 남은 무게 < 넣을 물건
for i in range(1,n+1):
    for j in range(1,k+1):
        w = lst[i][0]
        v = lst[i][1]
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        
print(dp[n][k])
 
 #그렇지 않을경우
 #1. 배낭에 현재 물건을 넣는다
 #2. 이전배낭 그대로 간다.   
 
    
    