import sys
sys.setrecursionlimit(500000)

def check_up_is_safe(i, j, rain, ddang, ddang2, ddang3, cnt):
    if 0 <= i-1 < N:
        if ddang[i-1][j]>rain:
            ddang2[i-1][j] = cnt
            ddang3[i-1][j] = True
            check_is_safe(i-1,j, rain, ddang, ddang2, ddang3, cnt)
           
            
def check_down_is_safe(i, j, rain, ddang, ddang2, ddang3, cnt):
    if 0 <= i+1 < N:
        if ddang[i+1][j]>rain:
            ddang2[i+1][j] = cnt
            ddang3[i+1][j] = True
            check_is_safe(i+1,j, rain, ddang, ddang2, ddang3, cnt)


def check_right_is_safe(i, j, rain, ddang, ddang2, ddang3, cnt):
    if 0 <= j+1 < N:
        if ddang[i][j+1]>rain:
            ddang2[i][j+1] = cnt
            ddang3[i][j+1] = True
            check_is_safe(i,j+1, rain, ddang, ddang2, ddang3, cnt)


def check_left_is_safe(i, j, rain, ddang, ddang2, ddang3, cnt):
    if 0 <= j-1 < N:
        if ddang[i][j-1]>rain:
            ddang2[i][j-1] = cnt
            ddang3[i][j-1] = True
            check_is_safe(i,j-1, rain, ddang, ddang2, ddang3, cnt )


def check_is_safe(i, j, rain, ddang, ddang2, ddang3, cnt):
    if j+1 < N and not ddang3[i][j+1]:
        check_right_is_safe(i,j, rain, ddang, ddang2, ddang3, cnt)
    if i+1 < N and not ddang3[i+1][j]:
        check_down_is_safe(i,j, rain, ddang, ddang2, ddang3, cnt)
    if 0 <= j-1 and not ddang3[i][j-1]:
        check_left_is_safe(i,j, rain, ddang, ddang2, ddang3, cnt)
    if 0 <= i-1 and not ddang3[i-1][j]:
        check_up_is_safe(i,j, rain, ddang, ddang2, ddang3, cnt)

N=int(input())
ddang=[]
max_num = []
for _ in range(N):
    ddang.append(list(map(int, input().split())))


for rain in range(0, max(map(max, ddang))+1):
    # print(rain)
    cnt = 0
    ddang2=[ [0]*N for _ in range(N) ]
    ddang3=[ [False]*N for _ in range(N) ] 
    for i in range(N):
        for j in range(N):
            # 처리되었는지 체크
            if ddang3[i][j] == False:
                # 처리하였음을 확인
                ddang3[i][j] = True
                # 현재 안전지대인지 확인 후 분류
                if ddang[i][j] > rain and ddang2[i][j] == 0:
                    # print(f"processing ddang[{i}][{j}]")
                    cnt += 1
                    ddang2[i][j] = cnt
                    # 안전지대인 경우 주변 값 찾아봄
                    check_is_safe(i, j, rain, ddang, ddang2, ddang3, cnt)
                    

                elif ddang[i][j] <= rain:
                    ddang2[i][j] = -1

    for i in range(N):
        # print(ddang2[i])
        max_num.append(max(ddang2[i]))
    # print()

print(max(max_num, default=1))