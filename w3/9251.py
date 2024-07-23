import sys 
input = sys.stdin.readline
# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
X = input().strip()
Y = input().strip()
h, w = len(X), len(Y)
LCS = [[0] *(w+1) for _ in range(h+1)]


# 그런데 점화식을 사용하기 위해서는 i-1, j-1이 사용되어야 하므로,
# 행렬에서 0으로 구성된 한 행과 한 열을 추가해준다.
for i in range(1, h+1):
    for j in range(1, w+1):
        if X[i-1] == Y[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else :
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
print(LCS[h][w])