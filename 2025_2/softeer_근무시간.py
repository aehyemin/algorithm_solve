import sys
t = []
input = sys.stdin.readline
for i in range(5):
    t.append(list(input().split()))

time = []

for i in t:
    hour, m = i[0].split(':')
    a_hour, a_m = i[1].split(':')
    hour, m = int(hour), int(m)
    a_hour, a_m = int(a_hour), int(a_m)
    time.append((a_hour*60 + a_m) - (hour*60 + m))


print(sum(time))
    