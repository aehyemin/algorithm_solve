T = int(input())
another_t = T
A = 0
B = 0
C = 0

while (T > 0) :
    if T >= 300 :
        A = another_t // 300 # 몫
        
        T = T % 300
        
       
    if T >= 60 and T < 300 :
        B = T // 60
        T = T % 60
        
        
    if T >= 10 and T < 60 : 
        C = T // 10
        T = T % 10
    else :
        break
        
       

if T == 0 :
    print(A, B, C)
else :
    print(-1)
    
