from collections import deque
#N은 지도의 크기 (N*N)
N = int(input())
graph = []

#다음N줄에 각각N개의 자료(0또는1)
for i in range(N):
    graph.append(input())
    
def dfs(x,y):
    count = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(N):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1:
            count += 1
            dfs(nx, ny)
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = 1
            # 이 줄은 연결된 영역의 크기를 세기 위한 카운터를 초기화
            # 현재 위치 maps[i][j]에서 1을 발견했기 때문에, 
            # 처음 시작할 때는 최소한 현재 위치 하나를 포함하여
            # cnt를 1로 설정 
            # 현재 위치가 연결된 영역의 시작점임을 나타내기 위해
            # 초기값을 1로 설정
            graph[i][j] = 0 #현재 위치를 0으로 바꾸어 방문표시함(더이상방문 못하게 만듦)
            count = dfs(i, j)
            result.append(count)

print(len(result))
result.sort()
for k in result:
    print(k)

#출력
#첫번째줄에는 총 단지수
#다음줄부터는 단지내 집의 수 오름차순