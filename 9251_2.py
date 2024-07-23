X = input()
Y = input()
w, h = len(X), len(Y)

LCS = [[0]*(w+1) for i in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if X[j-1] == Y[i-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else :
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[h][w])
