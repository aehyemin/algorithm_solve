from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
w, b = 0, 0

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt 


for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            ans = bfs(i, j)
            if graph[i][j] == 'W':
                w += ans ** 2
            else: 
                b += ans ** 2
print(w, b)
                
    