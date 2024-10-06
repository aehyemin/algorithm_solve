X = input()
Y = input()
LCS = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
for i in range(1, len(X)+1):
    for j in range(1, len(Y)+1):
        if X[i-1] == Y[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else :
            LCS[i][j] = max( LCS[i-1][j], LCS[i][j-1])
print(LCS[len(X)][len(Y)])
        
            
            