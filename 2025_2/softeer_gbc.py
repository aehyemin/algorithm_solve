import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = [0] * 101
r_lst = [0] * 101

now = 1
for i in range(n):
    street, limit = map(int, input().split())
    for j in range(now, now + street):
        lst[j] = limit
    now = now + street

now = 1
for i in range(m):
    r_street, r_limit = map(int, input().split())
    for j in range(now, now + r_street):
        r_lst[j] = r_limit
    now = now + r_street

speed = 0
for i in range(101):
    if r_lst[i] > lst[i]:
        speed = max(r_lst[i] - lst[i], speed)
if speed > 0:      
    print(speed)
else:
    print(0)
​