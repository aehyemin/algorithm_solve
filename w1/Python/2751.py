import sys
N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    sys.stdout.write(str(i) + '\n')
    # 입력출력만 바까주니까 도ㅓㅣ긴했는데 병합정렬사용하기