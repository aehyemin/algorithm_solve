import sys
from collections import deque

input = sys.stdin.readline


n = int(input())

data = deque(enumerate(map(int, input().split())))

result = []
while data:
    idx, turn = data.popleft()
    result.append(idx + 1)

    if turn > 0:
        data.rotate(-(turn-1))
    elif turn < 0:
        data.rotate(-turn)
        
print(' '.join(map(str, result)))