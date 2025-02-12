import sys
input = sys.stdin.readline
n= int(input())
a = input()

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(n+1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    #산책의 시작과 끝은 실내
    #중간에 실내면 안됨
    #산책 경로는 몇가지??