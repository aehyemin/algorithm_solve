import sys
sys.setrecursionlimit(10**5)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
w, b = 0, 0

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

def dfs(x, y):
    visited[x][y] =1
    c = graph[x][y]
    cnt = 1
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == c and visited[nx][ny] == 0:
                cnt += dfs(nx, ny)
    return cnt 


for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            ans = dfs(i, j)
            if graph[i][j] == 'W':
                w += ans ** 2
            else: 
                b += ans ** 2
print(w, b)
                
    