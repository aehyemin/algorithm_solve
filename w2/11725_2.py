N = int(input())
import sys
sys.setrecursionlimit(10**6)
visited = [0]*(N+1)
parent = [0]*(N+1)
graph = [ [] for i in range(N+1)]


for _ in range(1,N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def DFS(node):
    visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0:
            parent[i] = node
            DFS(i)
         
        
        
DFS(1)  
for j in range(2,N+1):
    print(parent[j])