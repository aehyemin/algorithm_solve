import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

maps = []

for i in range(n):
    maps.append(list(map(int, input().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    maps[x][y] = 0
    ans = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = 0
                ans += 1
    return ans
                


home_town = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home_town.append(bfs(i,j))

print(len(home_town))
for i in sorted(home_town):
    print(i)
    

        
        
       