#N개의 센서, K개의 집중국
#N개의 센서는 하나의 집중국과 연결되어있어야한다
#집중국의 수신 가능 영역의 길이의 합 최소화

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

distances = []
for i in range(1, N):
    distances.append(sensor[i]- sensor[i-1])

distances.sort(reverse=True)

for _ in range(K-1):
    if distances:
        distances.pop(0)
    
result = sum(distances)
print(result) 