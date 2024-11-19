from itertools import combinations
N, K = map(int, input().split())  #단어의 개수 N, 단어의 개수K
#N개의 줄에 남극 언어의 단어가 주어진다
# a n t i c 다섯글자는 필수로 가르쳐야 한다.
# k < 5 이면 출력 0 

origin = {"a", "n", "t", "i", "c"}
words = []

    
if K < 5:
    print(0)  
else : 
    words = [input().strip() for _ in range(N)]
    unique = set()
    
    for word in words:
        unique.update(words[4:-4])
        
    available = unique - origin
    max_cnt = 0
    # <= 연산자는 왼쪽 집합이 오른쪽 집합의 부분 집합인 경우 True를 반환합니다.
    for com in combinations(available, K - 5):  # K - 5개의 조합 생성
        cur_set = set(com) | origin  # 현재 조합 + 필수 글자
        
        # 읽을 수 있는 단어 수 계산
        cnt = 0
        for word in words:
            if all(char in cur_set for char in word):  # 모든 글자가 cur_set에 포함되는지 확인
                cnt += 1
                
        max_cnt = max(max_cnt, cnt)  # 최대 개수 업데이트

    print(max_cnt)  # 결과 출력
    
