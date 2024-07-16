import sys
input = sys.stdin.readline
#도시개수, 도로개수, 거리정보, 출발도시번호
N, M, K, X = map(int, input().split())

INF = 1e9
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    
def smallest():
    min_val = INF
    index = -1 
    for i in range(1,N+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i          
    return index
            
    
    
def dijkstra(start):
    distance[start] = 0
    for i in range(N):
        now = smallest()
        if now == -1:
            break
        visited[now] = True
        
        for j in graph[now]:
            if distance[now] + 1 < distance[j]:
                distance[j] = distance[now] + 1
            
       
    
    
    
dijkstra(X)
result = []
for i in range(1,N+1):
    if distance[i] == K:
        result.append(i)
        
if not result:
    print(-1)
else : 
    for city in result:
        print(city)
    
    
    
