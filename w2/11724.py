# 첫째줄에 정점의 개수N, 간선의 개수M
# 둘째줄부터 M개의 줄에 간선의 양 끝점 u 와 v가 주어진다. 같은 간선은 한번만 주어짐
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
# 인접 리스트 방식: graph = [[] for _ in range(N + 1)]
# 인접 행렬 방식: graph = [[0]*(N+1) for _ in range(N+1)]
graph = [ [] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split()) # u!=v
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)


def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0 :
            dfs(i)

component_count = 0
for i in range(1,N+1):
    if visited[i] == 0:
        component_count +=1
        dfs(i)
        

print(component_count)
            



    