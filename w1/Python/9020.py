# 골드 바흐 파티션 출력하기
'''
2보다 큰 짝수n가 주어졌을때 n은 두개의 소수의 합으로 나타낼수있다. - 골드바흐흑
파티션이 여러가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다
(입력) => 소수1 + 소수2 
소수2 - 소수1 = 0
소수1 = 소수2
방향성~?

골드바흐 파티션을 출력할건데
골드바흐 파티션은 소수 1 + 소수 2 = 특정 짝수 값
내가 어떤 조건을 체크한다음에 ok  하고 내보낼거야
그게뭐야?
소수인지 확인해야 돼

혜) 소수인지 확인하고 차를 체크한다
성) 차가 제일 작은 것부터 소수인지 확인한다

재사용할 것은?
소수인지 확인한다

파티션이 여러 개면 두 소수의 차이가 가장 작은 것을 출력한다.
= 두 소수의 차이가 가장 적은 것 부터 두 소수의 차이가 큰 방향으로 반복문을 진행한다.
시작점
차이가 가장 적은 두개의 수      를 찾아서 - 소수인지
소수1+소수2=num
절반부터시작
P1 + P2 = NUM
P2 = NUM - P1




'''
# 소수 확인
def is_prime(num:int) -> bool:
    
    for i in range(2,(num//2)+1):
        if num % i == 0:
            return False
        
    return True
    
    

# 4 4, 3 5, 
if '__name__' == '__main__':
    trial = int(input())
    for i in range(trial):
        num = int(input())
        p1 = num//2
        # is_prime(num) == true 면 (소수라는뜻) -> 모르겟땅 ??소수를두번
        while(True):
            if is_prime(p1) == True:
                if is_prime(num-p1) == True:
                    break
            p1 -= 1


    print(f"{p1} {num-p1}")







