#N은 N*N시험관의 크기, K는 바이러스 종류 가지수
N, M = map(int,input().split())
for i in range(N):
    V = map(int,input().split())
  
#X가 열:아래로|, Y가 행:오른쪽으로ㅡ
#S초 뒤에(X,Y)에 존재하는 바이러스의 종류
#존재하지 않으면 0을 출력    
S, X, Y = map(int,input().split())


