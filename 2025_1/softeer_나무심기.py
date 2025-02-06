import sys

input = sys.stdin.readline

n = int(input())

f = list(map(int, input().split()))
cnt = -10000
#토양의 비옥함 f_a * f_b
for i in range(1, n):
    for j in range(i):
        if f[i] * f[j] > cnt:
            cnt = f[i] * f[j]
print(cnt)