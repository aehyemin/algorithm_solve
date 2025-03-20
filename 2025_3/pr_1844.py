from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue.append((0,0))
    

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
                    
                    
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1
            
        
    
  