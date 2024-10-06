import sys
input = sys.stdin.readline

#서류와 인터뷰 모두 자기보다 나은 사람이 있으면 컷
T = int(input())
for _ in range(T):
    N = int(input())
    grade = []
    for _ in range(N):
        doc, interview = map(int, input().split())
        grade.append((doc, interview))
    grade.sort()
        
    count = 1
    top = grade[0][1]
    for i in range(1, len(grade)):
        if top > grade[i][1]:
            count += 1
            top = grade[i][1]
    print(count)