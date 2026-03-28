def solution(x):
    score=0
    str_x = str(x)
    for i in str_x:
        score += int(i)
    if x % score == 0:
        return True
    else:
        return False
