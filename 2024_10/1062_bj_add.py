from itertools import combinations

#N개의 줄에 남극 언어의 단어가 주어진다
# a n t i c 다섯글자는 필수로 가르쳐야 한다.
# k < 5 이면 출력 0 

def main(word):
    bit = 0
    for char in word:
        bit = bit | (1<< ord(char) - ord('a'))
    return bit

N, K = map(int, input().split())
        
words = [input().strip() for _ in range(N)]
bits = list(map(main, words))
base = main('antic')

if K < 5:
    print(0)
    
else : 
    alphabet = [1 << i for i in range(26) if not (base & 1<< i)]
    answer = 0
    for com in combinations(alphabet, K-5):
        know_bit = sum(com) | base 
        cnt = 0
        for bit in bits:
            if bit & know_bit == bit :
                cnt+=1 
        answer = max(answer, cnt)
    print(answer)