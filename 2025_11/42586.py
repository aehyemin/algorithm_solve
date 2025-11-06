def solution(progresses, speeds):
    result = []
    for i in range(len(progresses)):
        ans = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            ans += 1
        result.append(ans)
        
    new = []
    #앞의 기능보다 앞설 수 없음. 같은 날에만. 더 빨리 개발되면 앞이 완성되는 날에 같이 배포해야함
    tmp = 1 #같이배포되는 수
    day = result[0]
    
    for i in range(1, len(result)):
        if day >= result[i]:
            tmp += 1
        else:
            new.append(tmp)
            day = result[i]
            tmp = 1
    new.append(tmp)
    return new
        
        

            
            
