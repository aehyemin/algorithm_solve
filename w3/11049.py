#첫째줄 행렬의 개수N
#둘째줄부터 N개 줄에 행렬의 크기 r과 c
#순서대로 곱셈
N = int(input())
graph = [] 
for _ in range(N):
    graph.append(list(map(int,input().split())))
  
dp = [[0]* N for _ in range(N)]

for i in range(1,N): # i는 간격에 따른 대각선 줄
    for j in range(N-i): # j는 대각선의 항목
        x = i + j
        dp[j][x] = float('inf')
        
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + graph[j][0]*graph[k][1]*graph[x][1])
print(dp[0][N-1])       