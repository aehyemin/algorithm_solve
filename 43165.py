# def solution(numbers, target):
#     stack = [(0, 0)]
#     cnt = 0
    
#     while stack:
#         idx, total = stack.pop()
#         if len(numbers) == idx:
#             if total == target:
#                 cnt += 1
#             continue
#         stack.append((idx+1, total + numbers[idx]))
#         stack.append((idx+1, total - numbers[idx]))        
#     return cnt
# def solution(numbers, target):
    
#     def dfs(idx, total):
#         if idx == len(numbers):
#             if total == target:
#                 return 1
#             else: 
#                 return 0
            
        
#         return (dfs(idx+1, total + numbers[idx]) +dfs(idx+1, total - numbers[idx]))
        
        
#     return dfs(0,0)
from collections import deque
def solution(numbers, target):
    q = deque()
    q.append((0,0))
    cnt = 0
    
    while q:
        idx, total = q.popleft()
        if len(numbers) == idx:
            if total == target:
                cnt += 1
            continue
        q.append((idx+1,total + numbers[idx]))
        q.append((idx+1,total - numbers[idx]))
        
        
    return cnt
