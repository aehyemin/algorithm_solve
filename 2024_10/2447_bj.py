N = int(input())
# N은 3의 거듭제곱이다
# N > 3 경우, 크기 N 의 패턴은 공백으로 채워진 
# 가운데의 (N/3) * (N/3) 정사각형을 크기 N/3 의 패턴으로 둘러싼 형태
#분할 , 정복 , 합치기


base = ['***', '* *', '***']

def star(l):
    if l == 3:
        return ['***', '* *', '***']
    arr = star(l//3)
    stars = []
    
    for i in arr:
        stars.append(i*3)
        
    for i in arr:
        stars.append(i + ' ' * (l//3) + i)
        
    for i in arr:
        stars.append(i*3)
        
    return stars
print('\n'.join(star(N)))