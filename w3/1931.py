#회의수N
# start, end 
meeting = []
start_time = 0
count = 0
N = int(input())
for _ in range(N):
    start, end = map(int,input().split())
    meeting.append((start,end))

meeting = sorted(meeting, key=lambda time: time[0])
meeting = sorted(meeting, key=lambda time: time[1])
# print(meeting)
for i in range(N):
    if meeting[i][0] >= start_time:
        start_time = meeting[i][1]
        count += 1
print(count)

