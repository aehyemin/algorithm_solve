import sys

input = sys.stdin.readline

n = int(input())
train =[]

#n개의 역과, n줄에 걸쳐서 x,y좌표
for i in range(n):
    train.append(list(map(int, input().split())))
    
min_t = 100000000

for j in range(n):
    min_t = min(train[j][1], min_t) 
    
for k in range(n):
    if train[k][1] == min_t:
        print(*train[k])

# print(train)