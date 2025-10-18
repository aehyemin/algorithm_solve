T = int(input())
for i in range(T):
    n = int(input())
    cube = list(input().split())
    left = 1
    right = n-1
    ok = 0
    while left <= right:
        if cube[left] > cube[left-1] and cube[right] < cube[right-1]:
            break
        left += 1
        right -= 1
        ok += 1
 
    if ok == n//2:
        print("Yes")
    else:
        print("No")

 ####################################################################
from collections import deque
T = int(input())
for i in range(T):
    n = int(input())
    cube = deque(map(int, input().split()))
    ok = True
    top = float('inf')
    while cube:
        left = cube[0]
        right = cube[-1]
        if left <= right:
            pick = right
        else:
            pick = left
        if pick <= top:
            top = pick
            if pick == left:
                cube.popleft()
            else:
                cube.pop()
                
        else:
            ok = False
            break
            
    if ok == True:
        print("Yes")
    else:
        print("No")    
            
            

            
        
