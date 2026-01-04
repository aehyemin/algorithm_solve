#1-6번줄, 각 줄 당 1-P까지 나누어짐
#한 줄의 여러 프렛을 누르면, 가장 높은 음 발생
#손가락 떼는 횟수를 최소화하기
#높은 음 -> 낮은음은 손가락 +2, 낮은음 -> 높은음은 +1
n, p = map(int, input().split())


moves = 0
line = [[] for _ in range(7)] #[[1번줄], [2번줄..]..., [6번줄]]

for i in range(n):
    l, fret = map(int, input().split())

    while line[l] and line[l][-1] > fret:
        line[l].pop()
        moves += 1
    if not line[l] or line[l][-1] < fret:
        line[l].append(fret)
        moves += 1
print(moves)