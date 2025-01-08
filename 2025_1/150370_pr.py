def solution(today, terms, privacies):
    day = list(map(int, today.split('.')))
    today = day[0]*12*28 + day[1]*28 + day[2]
    
    dict = {}
    answer = []
    for i in terms:
        type, month = i.split()
        dict[type] = int(month) * 28
        
    for k in range(len(privacies)):
        p_start, p_type = privacies[k].split()
        p_date = list(map(int, p_start.split('.')))
        p_today = p_date[0]*12*28 + p_date[1]*28 + p_date[2]
        
        if today >= p_today + dict[p_type] :
            answer.append(k+1)

    return answer