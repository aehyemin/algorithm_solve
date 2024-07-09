def count_jongi(x,y,n):
    global white, blue
    color = jongi[x][y]

    for i in range(x, x+n): #
        for j in range(y, y+n):
            if jongi[i][j] != color: #color 는 검사를 시작한 영역의 색
                half = n // 2
                count_jongi(x, y, half)
                count_jongi(x, y + half, half)
                count_jongi(x + half, y, half)
                count_jongi(x + half, y + half, half)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

 
###################################################
N = int(input())
jongi = []
for _ in range(N):
    jongi.append(list(map(int,input().split())))

white = 0 
blue = 0

count_jongi(0, 0, N)
print(white)
print(blue)