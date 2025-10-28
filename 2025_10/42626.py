import heapq
def solution(scoville, K):
    #두개를 꺼내서 하나로 만든다음 넣기
    heapq.heapify(scoville)
    ans = 0
    #가장 작은값이 k이상이고 2개이상 요소가 있어야함
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new = a + b*2
        heapq.heappush(scoville, new)
        ans += 1
    return ans
        

