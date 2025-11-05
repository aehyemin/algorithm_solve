def solution(clothes):
    hash = {}
    
    for i in range(len(clothes)):
        name, part = clothes[i][0], clothes[i][1]
        
        if part not in hash:
            hash[part] = 1
        else:
            hash[part] += 1
            
    new = 1
    for i in hash.values():
            new *= (i+1)
    return new - 1
    
