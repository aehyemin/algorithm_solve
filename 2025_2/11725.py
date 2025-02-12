import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for i in range(n+1)]
parent = [0] * (n+1)
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    
def bfs(node):
    q = deque()
    q.append(node)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if parent[i] == 0:
                parent[i] = now
                q.append(i)
                
bfs(1)  
for i in range(2,n+1):
    print(parent[i])
# # print(graph)
   
 
# #각 줄의 부모 노드 번호를 2번 노드부터 출력
# def dfs(node):
#     for i in graph[node]:
#         if parent[i] == 0:  #정점의 연결된 i노드의 부모가 0이면
#             parent[i] = node
#             dfs(i)
# dfs(1)

# for i in range(2,n+1):
#     print(parent[i])