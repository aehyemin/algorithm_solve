import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))

for i in range(k):
    a,b = map(int, input().split())
    avg = sum(score[a-1:b])
    avg_f= (float)(avg/(b-a+1))
    print(round(avg_f, 2))
    
