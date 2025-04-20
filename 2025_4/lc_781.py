class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #n마리의 토끼들에서 너와 같은 색을 가진 토끼는 몇마리니 물었다
        #i번째 답변은 i번쨰 토끼의 대답
        #숲에 있는 토끼의 최소수
        cnt = 0
        hash={}
        for i in range(len(answers)):
            if answers[i] not in hash:
                hash[answers[i]] = 1
            else:
                hash[answers[i]] += 1

        for i, idx in hash.items():
            group = i + 1
            groups = math.ceil(idx / group)
            cnt += groups * group
            
        return cnt
