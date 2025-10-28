def solution(participant, completion):
    par = {}
    for i in participant:
        if i not in par:
            par[i] = 1
        else:
            par[i] += 1
            
    for j in completion:
        par[j] -= 1
        
    for k, idx in par.items():
        if idx != 0:
            return k
    # result = []
    # for k in par:
    #     if par[k] != 0:
    #         result.append(k)
    # return " ".join(result)
