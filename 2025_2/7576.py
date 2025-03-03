from collections import deque
import sys

m, n = map(int, input().split())
tomato = []

for i in range(n):
    tomato.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(tomato, n,m):
    q = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny] == 0:
                q.append((nx,ny))
                tomato[nx][ny] = tomato[x][y] + 1
    return tomato
                
tomato = bfs(tomato, n,m)


days = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    days = max(days, max(i))
print(days-1)