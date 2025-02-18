import sys
from collections import deque

input = sys.stdin.readline
n= int(input())
a = input().strip()
#정점에 대한 실내, 실외 정보를 저장한다.
#bfs
#산책경로 ans 
visited = [0] * (n+1)
ans = 0
def dfs(node, state, parent):
    global ans
    #첫번째 노드가 실내
    #중간은 다 실외 = 0
    #마지막 노드도 실내 = 1
    #실내1 -> 실외0 -> 실내1
    #실내1 -> 실내1
    for next in graph[node]:
        if next == parent:
            continue
        if state == 0:
            if a[next-1] == '1':
                ans += 1
            elif a[next-1] == '0':
                dfs(next, 1, node)
        else:
            if a[next-1] == '1':
                ans+=1
            elif a[next-1] == '0':
                dfs(next,0,node)
            
                    
    return ans
                    
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    #산책의 시작과 끝은 실내
    #중간에 실내면 안됨
    #산책 경로는 몇가지??

for i in range(1, n+1):
    if a[i-1] == '1':
        dfs(i, 0, -1)
       
print(ans)
# print(graph)