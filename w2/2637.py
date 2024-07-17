import sys
input = sys.stdin.readline
from collections import deque
# 완제품의 번호 N ,1~N-1까지는 기본부품이나 중간부품의 번호
N = int(input())
indegree = [0]*(N+1)

# [0]으로 초기화하면 각 노드에 기본적으로 [0]이 포함됨
# 실제 연결 정보를 저장하는 데 문제발생
graph = [[] for i in range(N+1)] #연결정보
needs = [[0]*(N+1) for _ in range(N+1)] #각 제품을 만들때 필요한 부품
# M개의 줄에는 부품들 간 관계가 X,Y,K
# X를 만드는데 Y가 K개 필요하다. X = Y*K
# M = int(input())

for i in range(int(input())): # M개의 줄에
    X, Y, K = map(int,input().split())
# 해당 부품이, 어떤 중간 제품의 부품이 되는지 기록한다.
# ex 5 2 2 라면 2번 부품은 5번에게 2개 필요하므로 2번 부품의 인접행렬에 5번 인덱스에 2를 넣는다.
# Y부품은 X번 부품에게 K개 필요하다 
    graph[Y].append((X,K))
    indegree[X] += 1
# 기본제품은 다른 부품에 의해 만들어지는 것이 아니니까 진입차수가 0이다.   
def topology_sort():
    Q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
            
    while Q:
        now = Q.popleft()
        #현 제품의 다음단계번호, 현 제품 얼마나 필요한지
        for next, next_need in graph[now]:
            if needs[now].count(0) == N+1:
                needs[next][now] += next_need
            else:
                for i in range(1,N+1):
                    needs[next][i] += needs[now][i] * next_need
            
            indegree[next] -= 1
            if indegree[next] == 0:
                Q.append(next)
                
    for p in enumerate(needs[N]):
        if p[1] > 0:
            print(*p)
  
topology_sort()









#출력: 기본 부품의 번호 , 소요 개수
#중간 부품은 출력X, 기본 부품만