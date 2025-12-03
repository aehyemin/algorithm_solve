#R 뒤집기, D첫번째 버리기, 비어있는데D면에러, 
from collections import deque
T = int(input())

for i in range(T):
    p = input()
    n = int(input())
    new = input().strip()
    
    err = False
    
    if n == 0:
        num = deque()
    else:
        arr = new[1:-1].split(',')
        num = deque(arr)
    
    r_num = 0

   
    for j in range(len(p)):
        if p[j] == 'R':
            r_num += 1
        else: #D일 경우
            if len(num) == 0:
                print('error')
                err = True
                break
            else:
                if r_num % 2 == 0:
                    num.popleft()
                else:
                    num.pop()
                    
    if err:
        continue #나머지는 건너뜀 
                    
    if r_num % 2 == 0:                  
        print("[" + ','.join(num) + ']')      
    else:
        num.reverse()      
        print("[" + ','.join(num) + ']')    
