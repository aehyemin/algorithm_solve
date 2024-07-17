from collections import deque
#N은 행의 수, M은 열의 수
N, M = map(int, input().split())

# 인접 행렬
maze = []

for _ in range(N):
    maze.append(list(map(int,input())))
    
# 위,아래,왼쪽,오른쪽 
dx = [ 1, -1, 0, 0]
dy = [ 0, 0, 1, -1 ]

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4): #위아래왼오 확인
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:
                queue.append((nx,ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[N-1][M-1]
            
print(bfs(0,0))           
            