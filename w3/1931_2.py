N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start,end))
  
count = 0
start_time = 0
new = sorted(meeting, key = lambda x:(x[1], x[0]))
# 우선 정렬되는 기준 정렬을 나중에 입력해야 한다!!!!!!!
# 종료 시간을 기준으로 정렬, 종료시간이 같으면 시작 시간으로 정렬
for i in range(N):
    if new[i][0] >= start_time:
        start_time = new[i][1]
        count += 1

print(count)
