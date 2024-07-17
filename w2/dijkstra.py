n, m = map(int, input().split())
k = int(input())

graph = [[]for _ in range(n+1)] #1번 노드부터 시작하므로 하나더 추가

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    #출발노드, 도착노드, 가중치
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def smallest():
    min_val = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distace[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for i in range[start]:
        distance[i[0]] = i[1]
    
    for _ in range(n-1):
        now = smallest()
        visited[now] = True
        
        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
                
dijkstra(k)
print(distace)