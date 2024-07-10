def count_paper(x,y,n):
    global white, blue
    color = paper[x][y]

    for i in range(x, x+n): #
        for j in range(y, y+n):
            if paper[i][j] != color: #color 는 검사를 시작한 영역의 색
                half = n // 2
                count_paper(x, y, half)
                count_paper(x, y + half, half)
                count_paper(x + half, y, half)
                count_paper(x + half, y + half, half)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

 
###################################################
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int,input().split())))

white = 0 
blue = 0

count_paper(0, 0, N)
print(white)
print(blue)