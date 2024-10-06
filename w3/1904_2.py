import sys
input = sys.stdin.readline

N = int(input())

fibo = [0] * 1000001
fibo[1] = 1
fibo[2] = 2
for i in range(3, N+1):
    fibo[i] = ((fibo[i-1]+fibo[i-2])%15746)
    
print(fibo[N])

    