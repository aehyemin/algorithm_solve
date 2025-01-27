import sys

input = sys.stdin.readline

t = int(input())
n = []
for i in range(t):
    n.append(int(input()))

ans = []
for i in n:
    a = i // 5 # 2
    b = i % 5 # 2

    while(a>0):
        print("++++ ", end ="")
        a-=1
    while (b>0): 
        print("|", end ="")
        b-=1
    if a==0 and b == 0:
        print("")



