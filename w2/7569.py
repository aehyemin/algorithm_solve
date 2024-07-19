import sys
input = sys.stdin.readline
from collections import deque
# M은가로칸수,N은세로칸수,H는쌓아올려지는상자수
tomatos = []
M, N, H = map(int,input().split())

for _ in range(H): #N개의 줄이 H번 반복
    layer = []
    for _ in range(N):
        layer.append(list(map(int,input().split())))
    #1:익은토마토, 0:익지않은토마토, -1:토마토없음
    tomatos.append(layer)
# 위 아래 왼쪽 오른쪽 앞 뒤   
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

Q = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 1:
                Q.append((x,y,z))
                
def bfs():
    while Q:
        x, y, z = Q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y+ dy[i], z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatos[nz][ny][nx] == 0:
                tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
                Q.append((nx,ny,nz))
bfs()           
max_day = 0
for i in tomatos:
    for j in i:
        for k in j:
            if k ==0:
                print(-1)
                exit(0)
        max_day = max(max_day, max(j))
print(max_day - 1)
                