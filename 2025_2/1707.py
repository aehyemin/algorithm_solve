import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
def bfs(node):
    visited[node] = 1
    q = deque()
    q.append(node)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = -visited[now]
                q.append(next)
            else:
                if visited[next] == visited[now]:
                    return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    graph = [[]for i in range(v+1)]
    visited = [0] * (v+1)
    ok = True
    for i in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, v+1):
        if visited[i] == 0:
            if bfs(i) == False:
                ok = False
    print("YES" if ok== True else "NO")
            


#각 집합에 속한 정점끼리 서로 인접하지 않도록 분할할 수 있을때 - 이분그래프
