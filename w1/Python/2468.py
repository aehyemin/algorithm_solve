from collections import deque

def bfs(si,sj,h):
    q = deque()

    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        # 네방향,범위내,미방분,높이>h
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상 하 좌 우
            ni,nj = ci +di, cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and ddang[ni][nj]>h:
                q.append((ni,nj))
                visited[ni][nj]=1



def solve(h): # h 높이에 대해 잠기지 않는 영역 개수
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and ddang[i][j] > h:
                bfs(i,j,h)
                count+=1
    return count



N = int(input())
ddang = [] # map에 대한 정보
# visited = [] # 방문에 대한 정보
for _ in range(N):
    ddang.append(list(map(int,input().split())))


ans = 0
for h in range(100): # 높이 0 ~ 99
    visited = [[0]*N for _ in range(N)]
    ans = max(ans, solve(h))
print(ans)


# def dfs(x, y, h):
#     for i in range(4):
#         nx =  x + dx[i]
#         ny =  y + dy[i]
#         if


# for i in range(N):
#     for j in range(N):
#         if ddang[i][j] > N and visited[i][j]== 0 :
#             bfs(i,j) 
#             count+= 1
#             # if 영역 사이의 길이가 1이면 같은 영역이라고 한다
# return count




# 4방향, 범위내 0<=, <N v[ni][nj] == 0
# arr[ni][nj] > h



# print(count)
# print(here)




