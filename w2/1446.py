# 지름길의 개수N, 고속도로의길이D
#둘째줄부터 N개의 줄에 u,v,w=시작,도착,지름길의길이 주어짐

N, D =  map(int,input().split())
INF = 1e9

visited = [False] * (D+1)
graph = [[]for _ in range(D+1)]
distance = [INF] * (D+1)

for _ in range(N):
    u,v,w = map(int,input().split())
    if v <= D:
        graph[u].append((v,w))
    
def smallest():
    min_val = INF
    index = 0
    for i in range(D+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index
   

def dijkstra(start):
    distance[start] = 0

    for i in range(D+1):
        now = smallest()
        if distance[now] == INF:
            break
        visited[now] = True
    
    for _ in range(1,D+1):
        now = smallest()
        visited[now] = True
        
        for v,w in graph[now]:
            if distance[now] + w < distance[v]:
                distance[v] = distance[now] + w
                
        if now + 1 <= D and distance[now + 1] > distance[now] + 1:
            distance[now + 1] = distance[now] + 1
                
dijkstra(0)
print(distance[D])
            
    
    
    

    
