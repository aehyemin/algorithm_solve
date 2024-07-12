# 첫째 줄에 보드의 크기 N (2<=N<=100)
N = int(input())

# 둘째 줄에 사과의 개수 K (0<=K<=100)
K = int(input())
location = []
# 다음 K개의 줄에는 사과의 위치가 주어지는데, (첫번째 정수는 행-, 두번째 정수는 열 ㅣ)
for i in range(K):
    location.append(input().split())

# 다음 줄에는 뱀의 방향 변환 횟수 L
L = int(input())
direction = []
# 다음 L개의 줄에는 뱀의 방향 변환 정보. (정수 X, 문자 C)
for i in range(L):
    direction.append((input().split()))
# X 초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전
# 몇 초에 게임이 끝나는가?

#초랑 방향을 큐에 넣어야하나?