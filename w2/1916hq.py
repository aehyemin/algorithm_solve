import sys 
import heapq
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

def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0, start))
    distance[start] = 0
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        if dist > distance[now]:
            continue
        for next_city, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_city]:
                distance[next_city] = cost
                heapq.heappush(pq,(cost, next_city))
dijkstra(S)
print(distance[E])            