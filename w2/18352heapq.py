import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

INF = 1e9
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B,1))
    
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
                heapq.heappush(pq, (cost, next_city))
dijkstra(X)

result = []
for i in range(1, N + 1):
    if distance[i] == K:
        result.append(i)

if not result:
    print(-1)
else:
    for city in result:
        print(city)               
    