#첫번째줄: 테스트케이스의 개수 T
T = int(input())
#테스트케이스의 첫번째 줄에는 동전의 가지수N
#테스트케이스의 두번째 줄에는 N가지 동전의 금액이 오름차순으로 정렬
for i in range(T):
    N = int(input())
    coins= list(map(int,input().split()))    
#테스트케이스의 세번째 줄에는 만들어야할 금액
    goal = int(input())
    
# 목표 금액을 만들기 위한 경우의 수를 저장하는 배열
    d = [0] * (goal+1)
    d[0] = 1 
# 0원을 만드는 방법은 한가지
    
    
    for coin in coins:
        for j in range(coin, goal+1):
            d[j] += d[j - coin]
            
    print(d[goal])
                
   
    


#출력: N가지 동전으로 금액M을 만드는 모든 방법의 수를 한줄에 하나씩 출력
