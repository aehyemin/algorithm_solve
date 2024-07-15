import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# 테스트 케이스의 개수 K
K = int(input())

# 정점의 개수V, 간선의 개수E 
# E개의 줄에 걸쳐 간선에 대한 정보,
# 각 줄에 인접한 두 정점의 번호 u,v (u!=v)

#함수는 모든 코드를 실행하기 전에 정의되어 있어야 한다.

def dfs(graph,n,color):
    for neighbor in graph[n]:
        if color[neighbor] == -1:
            color[neighbor] = 1 - color[n]
            if not dfs(graph, neighbor, color):
                return False
        elif color[neighbor] == color[n]:
            return False        
    return True


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    color = [-1] * V
    is_bipartite = True
    
    
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    for i in range(V):
        if color[i] == -1:
            color[i] = 0
            if not dfs(graph,i,color):
                is_bipartite = False
                break
            
    print("YES" if is_bipartite else "NO")            

    
    
   

