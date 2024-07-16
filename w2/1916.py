import sys 
input = sys.stdin.readline
N = int(input()) #도시의 개수
M = int(input()) #버스의 개수

INF = 1e9
graph = [ [] for _ in range(N+1)]

for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    
S, E = map(int,input().split())

visited = [False] * (N+1)
distance = [INF] * (N+1)

def smallest():
    min_val = INF
    index = -1
    for i in range(1, N+1):
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            index = i
    return index
    



def dijkstra(start):
    distance[start] = 0 
    
    for _ in range(N):
        now = smallest()
        if now == -1:
            break
        visited[now] = True

        for v,w in graph[now]:
            if not visited[v]:
                new_dist = distance[now] + w 
                if new_dist < distance[v]:
                    distance[v] = new_dist



dijkstra(S)
print(distance[E])