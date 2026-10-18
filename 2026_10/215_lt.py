import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        q = []
        for i in nums:
            heapq.heappush(q, i)
        
        for j in range(len(nums)-k):
            heapq.heappop(q)
        return q[0]
