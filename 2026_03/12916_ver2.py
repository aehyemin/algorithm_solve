def solution(s):
    s = s.upper()
    p_cnt = 0
    y_cnt = 0
    dict = {}
    for i in s:
        if i == "P":
            p_cnt += 1
        elif i == "Y":
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    return False
