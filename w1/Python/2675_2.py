T = int(input())

for _ in range(T):
    R, S = map(str, input().split())

    R = int(R)
    S = str(S)
    P =""

    for i in range(len(S)):
        P += S[i] * R
    print(P)

# S = input()

