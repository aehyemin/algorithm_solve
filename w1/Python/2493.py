from collections import deque
import sys

N = int(input())
# input = int(sys.stdin.readline())
stack = deque()
height = deque(map(int, input().split()))
# print(height)
ans = [0] * N

for i in range(N-1, -1, -1):
    #stack이 비버있지 않고, 현재탑의 높이가 스택의 맨 위 탑의 높이보다 큰 경우
    while stack and height[stack[-1]] < height[i] :
        ans[stack.pop()] = i+1 #pop() 스택의 맨 꼭대기에서 데이터를 꺼내서 반환
    stack.append(i)
print(*ans)
#  앞에 붙은 *은 포장을 일일이 풀어준다






        
        # while stack and stack[-1][0] < height[i]:
        #      stack.pop

        # if stack:
        #     result[i] = stack[-1][1]
        # stack.append(height[i])
        # if height[i] > height[i+1]:
        #     print(i)

        #     # ans.append(height[i+1] - height[i])
        # else :
        #     for k in list:
        #          if height[i] > height[k]:
        #               print(k)
            


