from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0] *(n+1)
    dis = [0] *(n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = 1
        dis[start] = 1
        while q:
            x = q.popleft() #1이면 graph[1] 방문
            for next in graph[x]: # 3, 2 를 돌면서 확인
                if visited[next] == 0:
                    visited[next] = 1
                    q.append(next)
                    dis[next] = dis[x] + 1
        
    bfs(1)
    max_num = max(dis)
    ans = 0
    return dis.count(max_num)
        
