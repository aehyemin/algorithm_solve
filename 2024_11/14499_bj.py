# r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수
#첫째줄의 세로크기N, 가로크기M, 주사위 놓은 곳의 좌표 x,y, 명령의 개수K
n, m, x, y, K = map(int, input().split())

board = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0, 0, 0, 0, 0, 0]

#동,서,남,북 으로 굴렸을때의 경우 4가지
def roll(n):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    #우로 굴렸을때,n=1 (1,2,3,4,5,6)=>(4,2,1,6,5,3)
    if n == 1: 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    
    #좌로 굴렸을때,n=2 (1,2,3,4,5,6)=>(3,2,6,1,5,4)
    elif n == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    
    #위로 굴렷을때, (1,2,3,4,5,6)=> (5,1,3,4,6,2)
    elif n == 3:
       dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    
    elif n == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
                
for i in range(n):
    board.append(list(map(int, input().split())))
    
command = list(map(int, input().split()))

nx, ny = x, y
for i in command:
    nx += dx[i-1]
    ny += dy[i-1]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    roll(i)
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else :
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
        
    print(dice[0])
