import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
A = '0' + input() #10111
# 노드 번호를 인덱스로 접근하기 위해 앞에 0 붙임

visited = [0]*(N+1)
graph = [ [] for i in range(N+1)]
total = 0
for _ in range(N-1):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    #실외를 거치지 않는 경우. 실내 - 실내
    if A[u] == "1" and A[v] == "1":
        total += 2
    
    
def dfs(start):
    visited[start] = 1
    in_count = 0 # 현재 노드와 인접한 실내 노드 개수를 저장할 변수
    
    for i in graph[start]:
            # 실외가 하나인 경우
        if A[i] == "1": # 인접한 노드가 실내면
            in_count += 1
            # 실외가 두개 이상
        elif visited[i] == 0 and A[i] == "0": # 실외 인접노드 실외면
            in_count += dfs(i)
                         
    return in_count

for j in range(1,N+1):
    if A[j] == "0" and visited[j] == 0 :
        result = dfs(j) #인접한 실내 노드 개수 계산
        total += result * (result - 1)
        
print(total)