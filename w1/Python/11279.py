import sys
import heapq

heap = []
N = int(input())

# for i in range(N):
#     heap.append(int(sys.stdin.readline()))


for _ in range(N):
    n = int(sys.stdin.readline())

    if n > 0:
        heapq.heappush(heap, -n)

    elif n == 0 :
        if heap:
            print(-heapq.heappop(heap))
        else :
            print(0)

    
# print(heap)

# for i in range(len(heap)):
#     max_heap.append(-heapq.heappop(heap))
# print(max_heap)


# if x 가 자연수이면 append(x)
# if x >= 0 :
#     heapq.heappush(heap, -x)

#if x==0 : 배열에서 가장 큰 값 출력하고 그 값을 배열에서 제거
# x <= 2**31



